# backend/main.py
import sqlite3
import re
import sys 
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal

# --- AÑADIDO: Importaciones para Monitorización ---
from prometheus_fastapi_instrumentator import Instrumentator
from loguru import logger

# LangChain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama.llms import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough

# --- AÑADIDO: CONFIGURACIÓN DE LOGGING ESTRUCTURADO ---
logger.remove()
logger.add(sys.stdout, serialize=True, enqueue=True)

class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        logger.log(level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
logging.getLogger("uvicorn").handlers = [InterceptHandler()]
logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]


# --- CONFIGURACIÓN Y MODELOS ---
VECTOR_STORE_DIR = "vector_store"
DB_PATH = "data/tickets.db"
app = FastAPI(title="Corporate EPIS Pilot API - Advanced Flow")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# --- AÑADIDO: INSTRUMENTACIÓN DE PROMETHEUS ---
Instrumentator().instrument(app).expose(app)


# Ajustar temperatura para smollm:360m - modelo pequeño funciona mejor con temperatura ligeramente mayor
llm = OllamaLLM(model="smollm:360m", temperature=0.3, base_url="http://host.docker.internal:11434")
embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")
vector_store = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embeddings)
retriever = vector_store.as_retriever()

# --- LÓGICA DE LANGCHAIN (MODIFICADA) ---
# Prompt simplificado para smollm:360m - más directo y claro
rag_prompt_template = """Responde la pregunta usando el contexto. Responde en español, de forma breve y clara.

Contexto: {context}

Pregunta: {question}

Respuesta:"""
rag_prompt = PromptTemplate.from_template(rag_prompt_template)
rag_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, chain_type_kwargs={"prompt": rag_prompt})

def create_support_ticket(description: str) -> str:
    """Crea un ticket de soporte y devuelve un mensaje de confirmación."""
    import os
    # Asegurar que el directorio existe
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT NOT NULL
    )
    ''')
    conn.commit()
    
    problem_description = description.replace("ACTION_CREATE_TICKET:", "").strip()
    if not problem_description:
        problem_description = "Problema no especificado por el usuario."

    cursor.execute("INSERT INTO tickets (description, status) VALUES (?, ?)", (problem_description, "Abierto"))
    ticket_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return f"De acuerdo. He creado el ticket de soporte #{ticket_id} con tu problema: '{problem_description}'. El equipo técnico se pondrá en contacto contigo."

# El router ahora es más simple
# CAMBIO 1: Añadimos la nueva intención 'despedida'
class RouteQuery(BaseModel):
    intent: Literal["pregunta_general", "reporte_de_problema", "despedida"] = Field(description="La intención del usuario.")

output_parser = JsonOutputParser(pydantic_object=RouteQuery)
# Prompt simplificado para smollm:360m - modelo pequeño necesita instrucciones muy claras
router_prompt = PromptTemplate(
    template="""Clasifica la pregunta en una sola palabra: pregunta_general, reporte_de_problema, o despedida.

Reglas:
- pregunta_general = pregunta de información (qué, cómo, cuántos)
- reporte_de_problema = problema o algo roto
- despedida = gracias o adiós

Pregunta: {question}

Responde SOLO con este formato exacto (sin nada más):
{{"intent": "pregunta_general"}}""",
    input_variables=["question"],
)
def extract_json_from_string(text: str) -> str:
    # Normalizar comillas simples a dobles y limpiar espacios
    text = text.replace("'", '"').strip()
    
    # Buscar JSON con comillas dobles
    match = re.search(r'\{"intent":\s*"[\w_]+"\}', text)
    if match:
        return match.group(0)
    
    # Buscar JSON con comillas simples (ya normalizado)
    match = re.search(r'\{[^{}]*"intent"[^{}]*\}', text)
    if match:
        json_str = match.group(0)
        # Normalizar comillas simples a dobles si es necesario
        json_str = json_str.replace("'", '"')
        # Asegurar que el valor de intent esté entre comillas
        json_str = re.sub(r'("intent"\s*:\s*)(\w+)', r'\1"\2"', json_str)
        return json_str
    
    # Si no encuentra JSON válido, intentar inferir desde palabras clave
    text_lower = text.lower()
    if any(word in text_lower for word in ['problema', 'roto', 'no funciona', 'error', 'falla']):
        return '{"intent": "reporte_de_problema"}'
    if any(word in text_lower for word in ['gracias', 'adiós', 'adios', 'perfecto', 'vale', 'ok']):
        return '{"intent": "despedida"}'
    
    return '{"intent": "pregunta_general"}'

router_chain = router_prompt | llm | RunnableLambda(extract_json_from_string) | output_parser

chain_with_preserved_input = RunnablePassthrough.assign(decision=router_chain)

problem_chain = RunnableLambda(lambda x: {"query": x["question"]}) | rag_chain

# --- ENDPOINT DE LA API (MODIFICADO) ---
@app.get("/ask")
def ask_question(question: str):
    try:
        if question.startswith("ACTION_CREATE_TICKET:"):
            description = question.split(":", 1)[1]
            return {"answer": create_support_ticket(description), "follow_up_required": False}

        # SOLUCIÓN RÁPIDA: Detectar directamente cuando el usuario quiere un ticket
        question_lower = question.lower()
        ticket_keywords = ["quiero un ticket", "necesito un ticket", "quiero ticket", "necesito ticket", "dame un ticket", "crear ticket", "generar ticket"]
        if any(keyword in question_lower for keyword in ticket_keywords):
            # Extraer descripción del problema si hay texto adicional
            description = question
            for keyword in ticket_keywords:
                if keyword in question_lower:
                    description = question.lower().replace(keyword, "").strip()
                    break
            if not description or len(description) < 3:
                description = "Solicitud de ticket de soporte"
            return {"answer": create_support_ticket(description), "follow_up_required": False}

        decision_result = chain_with_preserved_input.invoke({"question": question})
        intent = decision_result["decision"]["intent"]
        
        answer = ""
        follow_up = False

        if intent == "pregunta_general":
            result = problem_chain.invoke(decision_result)
            answer = result.get("result", "No se encontró respuesta.")
        elif intent == "reporte_de_problema":
            result = problem_chain.invoke(decision_result)
            solution = result.get("result", "No he encontrado una solución específica en mis documentos.")
            answer = f"{solution}\n\n¿Esta información soluciona tu problema?"
            follow_up = True
        # CAMBIO 3: Añadimos el manejo de la nueva intención
        elif intent == "despedida":
            answer = "De nada, ¡un placer ayudar! Si tienes cualquier otra consulta, aquí estaré. 😊"
            follow_up = False
            
        return {"answer": answer, "follow_up_required": follow_up}

    except Exception as e:
        # AÑADIDO: Usamos logger en lugar de print para un registro estructurado
        logger.error(f"Error en el endpoint /ask: {e}")
        return {"answer": "Lo siento, ha ocurrido un error.", "follow_up_required": False}