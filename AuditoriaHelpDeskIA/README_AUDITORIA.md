# INFORME FINAL DE AUDITORÍA DE SISTEMAS

## CARÁTULA

**Entidad Auditada:** Corporate EPIS Pilot - Sistema de Help Desk con Inteligencia Artificial  

**Ubicación:** [Ciudad, distrito, provincia, país]  

**Período auditado:** [Desde dd/mm/aaaa hasta dd/mm/aaaa]  

**Equipo Auditor:** Mirian Cuadros Garcia - 2021071083  

**Fecha del informe:** [dd/mm/aaaa]  

---

## ÍNDICE

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)  

2. [Antecedentes](#2-antecedentes)  

3. [Objetivos de la Auditoría](#3-objetivos-de-la-auditoría)  

4. [Alcance de la Auditoría](#4-alcance-de-la-auditoría)  

5. [Normativa y Criterios de Evaluación](#5-normativa-y-criterios-de-evaluación)  

6. [Metodología y Enfoque](#6-metodología-y-enfoque)  

7. [Hallazgos y Observaciones](#7-hallazgos-y-observaciones)  

8. [Análisis de Riesgos](#8-análisis-de-riesgos)  

9. [Recomendaciones](#9-recomendaciones)  

10. [Conclusiones](#10-conclusiones)  

11. [Plan de Acción y Seguimiento](#11-plan-de-acción-y-seguimiento)  

12. [Anexos](#12-anexos)  

---

## 1. RESUMEN EJECUTIVO

Esta auditoría de seguridad del sistema Corporate EPIS Pilot tuvo como objetivo evaluar la seguridad, integridad, disponibilidad y cumplimiento normativo del sistema de Help Desk asistido por Inteligencia Artificial. 

**Principales Hallazgos:**
La auditoría identificó **8 hallazgos** de los cuales **3 son de criticidad alta**, **4 de criticidad media** y **1 de criticidad baja**. Los hallazgos más críticos incluyen: (1) ausencia total de mecanismos de autenticación y autorización, (2) falta de estrategia de backup de bases de datos, y (3) inicialización frágil de base de datos que causa fallos de disponibilidad.

**Conclusiones:**
El sistema presenta una arquitectura sólida y uso innovador de IA, sin embargo, requiere implementación prioritaria de controles de seguridad y estrategia de continuidad antes de considerar su despliegue en producción. El cumplimiento normativo con ISO/IEC 27001:2022 y OWASP Top 10 es parcial, con incumplimientos significativos en controles de acceso y gestión de capacidad.

**Recomendaciones Prioritarias:**
1. Implementar sistema de autenticación y autorización (JWT/OAuth 2.0)
2. Establecer estrategia de backup automatizado de bases de datos
3. Corregir inicialización de base de datos para garantizar robustez
4. Restringir configuración CORS y implementar validación de entrada
5. Mejorar manejo de errores y logging para auditoría

**Evidencia:** [A completar]

---

## 2. ANTECEDENTES

El sistema Corporate EPIS Pilot es una aplicación de Help Desk asistida por Inteligencia Artificial diseñada para brindar soporte técnico a usuarios de EPIS Corp. El sistema implementa una arquitectura RAG (Retrieval-Augmented Generation) utilizando el modelo de lenguaje `smollm:360m` mediante Ollama para proporcionar respuestas contextualizadas basadas en documentación interna de la empresa.

**Características principales del sistema:**
- Arquitectura basada en microservicios (Frontend React, Backend FastAPI)
- Base de datos vectorial (ChromaDB) para almacenamiento de conocimiento
- Base de datos SQLite para gestión de tickets de soporte
- Despliegue mediante Docker y Docker Compose
- Integración con modelos de IA local (Ollama)
- Sistema de embeddings multilingüe (Hugging Face multilingual-e5-large)

**Antecedentes de auditorías previas:** [Indicar si existen auditorías previas o si esta es la primera]

**Evidencia:** [A completar]

---

## 3. OBJETIVOS DE LA AUDITORÍA

### 3.1. Objetivo General

**Evaluar la seguridad, integridad, disponibilidad y cumplimiento normativo del sistema Corporate EPIS Pilot, identificando riesgos y vulnerabilidades que puedan afectar la confidencialidad de la información, la continuidad del servicio y la calidad de la atención al usuario.**

**Evidencia:** [A completar]

---

### 3.2. Objetivos Específicos

#### Objetivo Específico 1: Evaluar la Seguridad de la Información y Protección de Datos Personales
Evaluar las medidas de seguridad implementadas para proteger la información almacenada en el sistema, incluyendo datos personales de usuarios, historiales de conversación y tickets de soporte. Verificar el cumplimiento de principios de confidencialidad, integridad y disponibilidad de la información.

**Evidencia:** [A completar]

---

#### Objetivo Específico 2: Evaluar la Disponibilidad y Continuidad del Servicio
Verificar la disponibilidad del sistema y las medidas implementadas para garantizar la continuidad del servicio de Help Desk, incluyendo evaluación de la infraestructura de despliegue (Docker, Kubernetes), redundancia de componentes y procedimientos de recuperación ante desastres.

**Evidencia:** [A completar]

---

#### Objetivo Específico 3: Evaluar la Integridad y Confiabilidad de los Datos Almacenados
Examinar la integridad de los datos almacenados en las bases de datos (SQLite para tickets y ChromaDB para conocimiento vectorial), verificando mecanismos de respaldo, recuperación de datos, validación de entrada y consistencia de la información.

**Evidencia:** [A completar]

---

#### Objetivo Específico 4: Evaluar el Cumplimiento de Buenas Prácticas de Desarrollo y Despliegue
Revisar la implementación del código, configuración de servicios, gestión de dependencias y despliegue del sistema, verificando el cumplimiento de estándares de desarrollo seguro, gestión de versiones, documentación técnica y prácticas de DevOps.

**Evidencia:** [A completar]

---

## 4. ALCANCE DE LA AUDITORÍA

### 4.1. Ámbitos Evaluados
- **Tecnológico:** Arquitectura, componentes de software, bases de datos, infraestructura de despliegue
- **Organizacional:** Procedimientos, documentación, roles y responsabilidades
- **Normativo:** Cumplimiento de estándares y mejores prácticas de seguridad

### 4.2. Sistemas y Procesos Incluidos
- Sistema de Help Desk (Frontend React + Backend FastAPI)
- Base de datos de tickets (SQLite)
- Base de datos vectorial de conocimiento (ChromaDB)
- Integración con modelo de IA (Ollama - smollm:360m)
- Sistema de embeddings (Hugging Face)
- Infraestructura de despliegue (Docker, Docker Compose, Kubernetes)
- Procesos de ingesta de documentación
- Flujos de creación y gestión de tickets

### 4.3. Unidades o Áreas Auditadas
- Código fuente del frontend (React/TypeScript)
- Código fuente del backend (Python/FastAPI)
- Configuraciones de despliegue (Docker, docker-compose.yml, Kubernetes manifests)
- Bases de datos y almacenamiento de datos
- Configuración de servicios externos (Ollama, Hugging Face)

### 4.4. Período Auditado
[Desde dd/mm/aaaa hasta dd/mm/aaaa]

**Evidencia:** [A completar]

---

## 5. NORMATIVA Y CRITERIOS DE EVALUACIÓN

### 5.1. Normas y Estándares Aplicados
- **COBIT 2019:** Marco de gobierno y gestión de tecnologías de la información
- **ISO/IEC 27001:2022:** Gestión de seguridad de la información
- **OWASP Top 10:** Principales vulnerabilidades de seguridad en aplicaciones web
- **CWE (Common Weakness Enumeration):** Clasificación de debilidades de software

### 5.2. Políticas y Mejores Prácticas
- Políticas internas de seguridad de TI de la entidad
- Mejores prácticas de desarrollo seguro (Secure Coding Practices)
- Estándares de despliegue en contenedores (Docker, Kubernetes)
- Mejores prácticas de gestión de datos personales

### 5.3. Criterios de Evaluación
- Confidencialidad, integridad y disponibilidad de la información (CIA)
- Cumplimiento de principio de menor privilegio
- Implementación de controles de seguridad adecuados
- Calidad del código y mantenibilidad
- Disponibilidad y recuperabilidad del servicio

**Evidencia:** [A completar]

---

## 6. METODOLOGÍA Y ENFOQUE

### 6.1. Enfoque Utilizado
Enfoque mixto basado en riesgos y cumplimiento normativo.

### 6.2. Métodos Aplicados
- **Entrevistas:** Con desarrolladores y responsables de TI
- **Inspección de documentos:** Revisión de código fuente, configuración y documentación
- **Pruebas técnicas:**
  - Análisis de código estático
  - Revisión de configuraciones de seguridad
  - Verificación de logs del sistema
  - Pruebas de funcionamiento del sistema
- **Revisión de configuraciones:** Docker, docker-compose, Kubernetes, servicios
- **Aplicación de listas de verificación:** Basadas en OWASP, CWE y mejores prácticas

**Evidencia:** [A completar]

---

## 7. HALLAZGOS Y OBSERVACIONES

### 7.1. Hallazgo 1: Falta de Inicialización Automática de Base de Datos en Ejecución
**Descripción del hallazgo:** La aplicación no garantiza la creación automática de la tabla `tickets` en la base de datos SQLite durante la ejecución del sistema. La inicialización solo se realiza durante el proceso de build del contenedor Docker mediante el script `database_setup.py`, lo que genera errores cuando la base de datos es montada como volumen o cuando el contenedor se reinicia sin reconstruirse.

**Evidencia objetiva:** 
- Error identificado en logs: `"Error en el endpoint /ask: no such table: tickets"`
- Código fuente `main.py` línea 66: Conexión directa a base de datos sin verificación previa de existencia de tablas
- El script `database_setup.py` solo se ejecuta durante el build del contenedor

**Grado de criticidad:** Alto

**Criterio vulnerado:** 
- ISO/IEC 27001:2022 - A.12.3.1 (Gestión de capacidad)
- Mejores prácticas de desarrollo - Inicialización robusta de recursos

**Causa:** 
- Falta de verificación y creación automática de estructura de base de datos en el código de la aplicación principal
- Dependencia exclusiva del script de inicialización durante el build de Docker
- No se contempla el escenario de volúmenes montados que pueden iniciarse vacíos

**Efecto:** 
- Fallos en la funcionalidad principal del sistema (creación de tickets)
- Pérdida de disponibilidad del servicio
- Necesidad de reconstruir contenedores para resolver el problema
- Impacto en la experiencia del usuario con errores del tipo "Lo siento, ha ocurrido un error"

---

### 7.2. Hallazgo 2: Configuración CORS Excesivamente Permisiva
**Descripción del hallazgo:** El backend FastAPI está configurado con CORS (Cross-Origin Resource Sharing) que permite cualquier origen (`allow_origins=["*"]`), lo que representa un riesgo de seguridad significativo al exponer la API a solicitudes desde cualquier dominio.

**Evidencia objetiva:** 
- Código fuente `main.py` líneas 45-48: `CORSMiddleware` configurado con `allow_origins=["*"]`, `allow_credentials=True`, `allow_methods=["*"]`, `allow_headers=["*"]`
- No existe restricción de orígenes permitidos
- No se implementa lista blanca de dominios autorizados

**Grado de criticidad:** Medio

**Criterio vulnerado:** 
- OWASP Top 10 - A05:2021 Security Misconfiguration
- ISO/IEC 27001:2022 - A.9.4.2 (Seguridad en equipos y puestos de trabajo)
- Principio de menor privilegio

**Causa:** 
- Configuración por defecto orientada a facilitar el desarrollo
- Falta de configuración específica para entornos de producción
- Ausencia de variables de entorno para gestión de orígenes permitidos

**Efecto:** 
- Posibilidad de ataques CSRF (Cross-Site Request Forgery)
- Exposición a solicitudes maliciosas desde cualquier dominio
- Riesgo de fuga de datos si se implementa autenticación en el futuro
- Vulnerabilidad a ataques de sitios web maliciosos

---

### 7.3. Hallazgo 3: Manejo Inadecuado de Respuestas del Modelo de IA
**Descripción del hallazgo:** El sistema presenta dificultades para procesar correctamente las respuestas del modelo de lenguaje `smollm:360m`, generando errores de parsing JSON que resultan en fallos silenciosos y mensajes genéricos de error al usuario, sin proporcionar información útil para diagnóstico.

**Evidencia objetiva:** 
- Errores en logs: `"Invalid json output: {'intent': pregunta_general, 'response': [pregunta_de_problema, pregunta_despedida]}"`
- El modelo devuelve JSON con comillas simples en lugar de dobles
- Mensajes de error genéricos: "Lo siento, ha ocurrido un error"
- Código fuente `main.py` líneas 115-142: Función `extract_json_from_string` con lógica de normalización implementada como workaround

**Grado de criticidad:** Medio

**Criterio vulnerado:** 
- ISO/IEC 27001:2022 - A.12.4.1 (Gestión de errores)
- Mejores prácticas de desarrollo - Manejo robusto de errores
- Usabilidad y calidad del servicio

**Causa:** 
- Modelo de lenguaje pequeño (360M parámetros) con limitaciones en la generación de JSON válido
- Falta de validación y normalización robusta de respuestas del modelo
- Manejo genérico de excepciones sin diferenciación de tipos de error
- Ausencia de fallback cuando el modelo falla

**Efecto:** 
- Degradación de la calidad del servicio
- Pérdida de confianza del usuario
- Necesidad de múltiples intentos para obtener respuesta
- Impacto negativo en la experiencia de usuario

---

### 7.4. Hallazgo 4: Falta de Validación de Entrada de Datos
**Descripción del hallazgo:** El endpoint `/ask` no implementa validación adecuada de los parámetros de entrada, aceptando cualquier valor sin restricciones de longitud, tipo o formato, lo que puede conducir a inyección de datos, sobrecarga del sistema o comportamientos inesperados.

**Evidencia objetiva:** 
- Código fuente `main.py` línea 157: Endpoint `@app.get("/ask")` con parámetro `question: str` sin validación
- No existe límite de longitud de entrada
- No se valida formato de caracteres permitidos
- No se implementa sanitización de entrada
- Datos del usuario se pasan directamente al modelo de IA sin filtrado

**Grado de criticidad:** Medio

**Criterio vulnerado:** 
- OWASP Top 10 - A03:2021 Injection
- ISO/IEC 27001:2022 - A.9.4.2 (Seguridad en equipos)
- Mejores prácticas de desarrollo seguro

**Causa:** 
- Confianza excesiva en la validación del framework
- Falta de implementación de esquemas de validación (Pydantic models)
- Priorización de funcionalidad sobre seguridad

**Efecto:** 
- Riesgo de inyección de prompts maliciosos al modelo de IA
- Posibilidad de provocar errores en el sistema mediante entradas inusualmente largas
- Potencial para exfiltración de información mediante prompts ingeniosos
- Sobrecarga del sistema con solicitudes maliciosas

---

### 7.5. Hallazgo 5: Ausencia de Mecanismos de Autenticación y Autorización
**Descripción del hallazgo:** El sistema no implementa ningún mecanismo de autenticación ni autorización, permitiendo acceso anónimo completo a todas las funcionalidades, incluyendo la creación de tickets y consulta de información sensible de la empresa.

**Evidencia objetiva:** 
- Revisión del código fuente: No se encontraron implementaciones de autenticación (JWT, OAuth, sessions)
- Endpoints públicos sin protección: `/ask`, `/metrics`
- Cualquier usuario puede crear tickets sin identificación
- No existe control de acceso basado en roles

**Grado de criticidad:** Alto

**Criterio vulnerado:** 
- ISO/IEC 27001:2022 - A.9.2.1 (Gestión de derechos de acceso)
- ISO/IEC 27001:2022 - A.9.2.2 (Provisión de acceso de usuario)
- OWASP Top 10 - A01:2021 Broken Access Control
- Principio de menor privilegio

**Causa:** 
- Arquitectura inicial enfocada en funcionalidad
- Falta de requisitos de seguridad en la fase de diseño
- Priorización de desarrollo rápido sobre seguridad

**Efecto:** 
- Acceso no autorizado a funcionalidades del sistema
- Imposibilidad de rastrear quién realiza acciones (auditoría)
- Riesgo de abuso del sistema (creación masiva de tickets)
- Exposición de información sensible sin control
- Vulneración de principios de confidencialidad e integridad

---

### 7.6. Hallazgo 6: Configuración Problemática de Volúmenes Docker
**Descripción del hallazgo:** La configuración inicial de Docker Compose intentaba montar un archivo de base de datos directamente (`tickets.db`) en lugar de un directorio, generando errores de montaje y problemas de persistencia de datos cuando el archivo no existe en el host.

**Evidencia objetiva:** 
- Configuración original `docker-compose.yml` línea 11: `- ./backend/tickets.db:/app/tickets.db`
- Error de Docker: `"error mounting tickets.db: not a directory"`
- Corrección implementada cambiando a montaje de directorio: `- ./backend/data:/app/data`
- Cambios en código para usar ruta `data/tickets.db`

**Grado de criticidad:** Bajo

**Criterio vulnerado:** 
- Mejores prácticas de Docker - Gestión de volúmenes
- ISO/IEC 27001:2022 - A.12.2.1 (Gestión de cambios)

**Causa:** 
- Configuración inicial inadecuada de volúmenes
- Falta de consideración del estado inicial de archivos montados
- Inexperiencia en configuración de persistencia de datos en Docker

**Efecto:** 
- Fallos en el despliegue del sistema
- Pérdida de persistencia de datos entre reinicios
- Necesidad de correcciones posteriores
- Impacto en la continuidad del servicio durante correcciones

---

### 7.7. Hallazgo 7: Falta de Estrategia de Backup de Bases de Datos
**Descripción del hallazgo:** El sistema no implementa ningún mecanismo automatizado de respaldo para las bases de datos (SQLite para tickets y ChromaDB para conocimiento vectorial), lo que representa un riesgo de pérdida de datos en caso de fallos de hardware, errores de software o eliminación accidental.

**Evidencia objetiva:** 
- Revisión del código: No se encontraron scripts de backup
- No existe configuración de backups automatizados en Docker Compose
- Falta de estrategia documentada de recuperación ante desastres
- Dependencia exclusiva de volúmenes Docker para persistencia

**Grado de criticidad:** Alto

**Criterio vulnerado:** 
- ISO/IEC 27001:2022 - A.12.3.1 (Gestión de capacidad)
- ISO/IEC 27001:2022 - A.12.3.2 (Aceptación de sistemas de desarrollo)
- COBIT 2019 - APO13.01 (Manejo de Backups)

**Causa:** 
- Falta de planificación de estrategia de respaldo
- Priorización de funcionalidad sobre continuidad del negocio
- Ausencia de requisitos de recuperación ante desastres

**Efecto:** 
- Pérdida total de datos en caso de fallo
- Imposibilidad de recuperación de información histórica
- Pérdida de conocimiento acumulado en la base vectorial
- Impacto crítico en la continuidad del negocio

---

### 7.8. Hallazgo 8: Logging Insuficiente para Auditoría y Seguridad
**Descripción del hallazgo:** Aunque el sistema implementa logging mediante Loguru, la información registrada no es suficiente para auditoría de seguridad, faltando logs de eventos críticos como intentos de acceso, creación de tickets, errores de seguridad y actividad del usuario.

**Evidencia objetiva:** 
- Logs actuales se enfocan en debug técnico (conexiones HTTP, respuestas de modelos)
- No se registran eventos de negocio (creación de tickets, consultas de usuarios)
- Ausencia de campos estándar para auditoría (usuario, IP, timestamp de eventos críticos)
- No se implementa correlación de eventos

**Grado de criticidad:** Medio

**Criterio vulnerado:** 
- ISO/IEC 27001:2022 - A.12.4.1 (Registro de eventos)
- ISO/IEC 27001:2022 - A.12.4.2 (Protección de información de registro)
- COBIT 2019 - EDM03.06 (Registro y Monitoreo)

**Causa:** 
- Enfoque en logging técnico para depuración
- Falta de requisitos de auditoría en el diseño
- Ausencia de políticas de logging de seguridad

**Efecto:** 
- Imposibilidad de rastrear actividad de usuarios
- Dificultad para investigar incidentes de seguridad
- Falta de cumplimiento de requisitos de auditoría
- Imposibilidad de detectar patrones de uso anormal o malicioso

---

## 8. ANÁLISIS DE RIESGOS

| Hallazgo | Riesgo Asociado | Impacto | Probabilidad | Nivel de Riesgo |
|----------|-----------------|---------|--------------|-----------------|
| 1        | Pérdida de disponibilidad del servicio debido a fallos en inicialización de base de datos | Alto | Media | Alto |
| 2        | Vulnerabilidad a ataques CSRF y acceso no autorizado desde dominios maliciosos | Medio | Alta | Medio |
| 3        | Degradación de calidad del servicio y pérdida de confianza del usuario | Medio | Alta | Medio |
| 4        | Inyección de datos maliciosos y potencial explotación del modelo de IA | Medio | Media | Medio |
| 5        | Acceso no autorizado, falta de trazabilidad y abuso del sistema | Alto | Alta | Alto |
| 6        | Pérdida de persistencia de datos y problemas en despliegue | Bajo | Media | Bajo |
| 7        | Pérdida total de datos sin posibilidad de recuperación | Alto | Media | Alto |
| 8        | Imposibilidad de auditoría, investigación de incidentes y detección de anomalías | Medio | Alta | Medio |

**Evidencia:** [A completar]

---

## 9. RECOMENDACIONES

### 9.1. Recomendación 1 (Asociada al Hallazgo 1): Implementar Inicialización Robusta de Base de Datos
**Descripción:** Implementar verificación y creación automática de estructura de base de datos en el código principal de la aplicación (función `create_support_ticket` y en un evento de inicio de la aplicación FastAPI). Utilizar el patrón "CREATE TABLE IF NOT EXISTS" para garantizar que las tablas existan independientemente del estado inicial de la base de datos. Implementar migraciones de base de datos mediante herramientas como Alembic para versionado de esquemas.

**Prioridad:** Alta

**Evidencia:** [A completar]

---

### 9.2. Recomendación 2 (Asociada al Hallazgo 2): Restringir Configuración CORS
**Descripción:** Modificar la configuración CORS para implementar una lista blanca de orígenes permitidos mediante variables de entorno. Configurar diferentes orígenes según el ambiente (desarrollo, staging, producción). Eliminar el uso de `allow_origins=["*"]` y restringir métodos y headers permitidos solo a los necesarios. Implementar validación de origen mediante middleware personalizado si se requiere lógica más compleja.

**Prioridad:** Alta

**Evidencia:** [A completar]

---

### 9.3. Recomendación 3 (Asociada al Hallazgo 3): Mejorar Manejo de Respuestas del Modelo de IA
**Descripción:** Implementar validación y normalización robusta de respuestas del modelo de IA. Agregar mecanismo de retry con fallback cuando el modelo falle. Mejorar los mensajes de error para proporcionar información útil sin exponer detalles técnicos. Considerar implementar un modelo de mayor capacidad para producción o establecer un pipeline de validación más estricto. Implementar logging detallado de errores del modelo para monitoreo.

**Prioridad:** Media

**Evidencia:** [A completar]

---

### 9.4. Recomendación 4 (Asociada al Hallazgo 4): Implementar Validación de Entrada
**Descripción:** Utilizar modelos Pydantic para validar parámetros de entrada del endpoint `/ask`. Establecer límites de longitud (máximo 1000 caracteres recomendado), validar formato de caracteres permitidos y sanitizar entrada antes de procesarla. Implementar rate limiting para prevenir abuso. Agregar validación de tipo y formato de datos en todos los endpoints.

**Prioridad:** Media

**Evidencia:** [A completar]

---

### 9.5. Recomendación 5 (Asociada al Hallazgo 5): Implementar Autenticación y Autorización
**Descripción:** Implementar sistema de autenticación mediante JWT (JSON Web Tokens) o OAuth 2.0. Requerir autenticación para todos los endpoints excepto endpoints públicos específicos. Implementar control de acceso basado en roles (RBAC) diferenciando entre usuarios regulares y administradores. Registrar todos los eventos de autenticación y acceso para auditoría. Implementar tokens de refresh para mejorar la seguridad.

**Prioridad:** Alta

**Evidencia:** [A completar]

---

### 9.6. Recomendación 6 (Asociada al Hallazgo 6): Mejorar Gestión de Volúmenes Docker
**Descripción:** Documentar correctamente la configuración de volúmenes Docker. Utilizar siempre directorios en lugar de archivos individuales para volúmenes montados. Implementar scripts de inicialización que verifiquen y creen estructura de directorios necesaria. Agregar documentación sobre gestión de volúmenes y persistencia de datos en el README del proyecto.

**Prioridad:** Baja

**Evidencia:** [A completar]

---

### 9.7. Recomendación 7 (Asociada al Hallazgo 7): Implementar Estrategia de Backup
**Descripción:** Implementar backups automatizados de ambas bases de datos (SQLite y ChromaDB) mediante scripts que se ejecuten periódicamente (recomendado diario). Almacenar backups en ubicación separada del sistema principal (almacenamiento en la nube o servidor remoto). Implementar pruebas periódicas de restauración de backups. Establecer retención de backups (mínimo 30 días, recomendado 90 días). Documentar procedimientos de recuperación ante desastres.

**Prioridad:** Alta

**Evidencia:** [A completar]

---

### 9.8. Recomendación 8 (Asociada al Hallazgo 8): Mejorar Logging para Auditoría
**Descripción:** Implementar logging estructurado para eventos de negocio y seguridad. Registrar todos los eventos críticos incluyendo: creación de tickets (con ID de usuario y detalles), consultas de usuarios, intentos de autenticación, errores de seguridad, cambios de configuración. Incluir campos estándar en todos los logs: timestamp, usuario, IP, acción, resultado. Implementar almacenamiento centralizado de logs (ELK stack o similar) y establecer retención mínima de 90 días para cumplir con requisitos de auditoría.

**Prioridad:** Media

**Evidencia:** [A completar]

---

## 10. CONCLUSIONES

### 10.1. Estado General del Sistema
El sistema Corporate EPIS Pilot presenta una arquitectura moderna y bien estructurada basada en microservicios, con separación clara entre frontend y backend. La implementación de RAG (Retrieval-Augmented Generation) para respuestas contextualizadas demuestra innovación en el uso de inteligencia artificial para atención al cliente. Sin embargo, la auditoría ha identificado varios aspectos críticos relacionados con seguridad, robustez y continuidad del servicio que requieren atención prioritaria antes de considerar el sistema como producción-ready.

El sistema funciona correctamente en escenarios ideales, pero presenta vulnerabilidades significativas en aspectos de seguridad (autenticación, CORS, validación de entrada) y robustez (inicialización de base de datos, manejo de errores, backups) que podrían comprometer la confidencialidad, integridad y disponibilidad de la información.

### 10.2. Aspectos Positivos
- **Arquitectura bien diseñada:** Separación clara de responsabilidades entre frontend y backend, facilitando mantenimiento y escalabilidad
- **Uso de tecnologías modernas:** Implementación de contenedores Docker, framework FastAPI, React con TypeScript, y modelos de IA locales
- **Implementación de RAG:** Sistema inteligente de respuestas basado en documentación interna de la empresa
- **Instrumentación de monitoreo:** Implementación de Prometheus para métricas del sistema
- **Logging estructurado:** Uso de Loguru para logging estructurado (aunque necesita mejoras para auditoría)
- **Código limpio y documentado:** Código fuente bien organizado y comentado

### 10.3. Aspectos Críticos Identificados
- **Ausencia total de autenticación y autorización:** El sistema es completamente público, permitiendo acceso anónimo a todas las funcionalidades
- **Falta de estrategia de backup:** No existe mecanismo de respaldo de datos, con riesgo de pérdida total de información
- **Inicialización frágil de base de datos:** Dependencia de scripts de build para creación de estructura, generando fallos en producción
- **Configuración de seguridad deficiente:** CORS excesivamente permisivo y falta de validación de entrada
- **Manejo inadecuado de errores del modelo de IA:** Falta de robustez en el procesamiento de respuestas del modelo pequeño

### 10.4. Cumplimiento Normativo
El sistema presenta incumplimientos significativos con las normativas aplicadas:

- **ISO/IEC 27001:2022:** Incumplimiento en controles de acceso (A.9.2.1, A.9.2.2), gestión de capacidad y backups (A.12.3.1), y registro de eventos (A.12.4.1)
- **OWASP Top 10:** Vulnerabilidades identificadas en categorías A01 (Broken Access Control), A03 (Injection), y A05 (Security Misconfiguration)
- **Principio de menor privilegio:** No aplicado, acceso público total al sistema
- **Cumplimiento parcial:** El sistema cumple parcialmente en aspectos técnicos y arquitectura, pero falla significativamente en controles de seguridad

Se requiere implementación de controles de seguridad antes de considerar el sistema como conforme con estándares de seguridad de la información.

### 10.5. Síntesis Evaluativa
Los controles existentes son **adecuados en aspectos funcionales y técnicos**, pero **insuficientes en aspectos de seguridad y robustez**. El sistema demuestra capacidad técnica para cumplir con sus objetivos funcionales (proporcionar asistencia técnica mediante IA), sin embargo, presenta deficiencias críticas que impiden su uso en un entorno de producción sin modificaciones significativas.

**Fortalezas:** Arquitectura sólida, código de calidad, uso innovador de IA, tecnologías modernas

**Debilidades:** Falta de controles de seguridad, ausencia de estrategia de continuidad, robustez insuficiente, cumplimiento normativo incompleto

**Recomendación General:** El sistema requiere implementación prioritaria de controles de seguridad (autenticación, validación, CORS) y estrategia de continuidad (backups, manejo de errores) antes de su despliegue en producción. Se estima que la implementación de las recomendaciones críticas requerirá un esfuerzo mínimo de 4-6 semanas de desarrollo.

**Evidencia:** [A completar]

---

## 11. PLAN DE ACCIÓN Y SEGUIMIENTO

| Hallazgo | Recomendación | Responsable | Fecha Comprometida | Estado |
|----------|---------------|-------------|---------------------|--------|
| 1        | Implementar inicialización robusta de base de datos | Equipo de Desarrollo Backend | [dd/mm/aaaa] | Pendiente |
| 2        | Restringir configuración CORS | Equipo de Desarrollo Backend | [dd/mm/aaaa] | Pendiente |
| 3        | Mejorar manejo de respuestas del modelo de IA | Equipo de Desarrollo Backend / IA | [dd/mm/aaaa] | Pendiente |
| 4        | Implementar validación de entrada | Equipo de Desarrollo Backend | [dd/mm/aaaa] | Pendiente |
| 5        | Implementar autenticación y autorización | Equipo de Desarrollo / Seguridad | [dd/mm/aaaa] | Pendiente |
| 6        | Mejorar gestión de volúmenes Docker | Equipo de DevOps | [dd/mm/aaaa] | Pendiente |
| 7        | Implementar estrategia de backup | Equipo de Infraestructura / DevOps | [dd/mm/aaaa] | Pendiente |
| 8        | Mejorar logging para auditoría | Equipo de Desarrollo Backend | [dd/mm/aaaa] | Pendiente |

### Priorización
- **Prioridad Alta (Implementación inmediata - 2 semanas):** Hallazgos 1, 2, 5, 7
- **Prioridad Media (Implementación - 4 semanas):** Hallazgos 3, 4, 8
- **Prioridad Baja (Mejora continua):** Hallazgo 6

**Evidencia:** [A completar]

---

## 12. ANEXOS

### Anexo A: Cuestionarios Aplicados
[Descripción y copia de cuestionarios utilizados en la auditoría]

**Evidencia:** [A completar]

---

### Anexo B: Capturas de Pantalla
[Descripción de capturas de pantalla relevantes]

**Evidencia:** [A completar]

---

### Anexo C: Registros de Logs
[Descripción de registros de logs analizados]

**Evidencia:** [A completar]

---

### Anexo D: Configuraciones Revisadas
[Descripción de archivos de configuración revisados]

**Evidencia:** [A completar]

---

### Anexo E: Revisión de Código Fuente
[Descripción de archivos de código fuente revisados]

**Evidencia:** [A completar]

---

### Anexo F: Políticas y Documentación Revisada
[Descripción de políticas y documentación técnica revisada]

**Evidencia:** [A completar]

---

### Anexo G: Información Técnica del Sistema

#### Stack Tecnológico
- **Backend:** Python 3.12, FastAPI, LangChain, Ollama (smollm:360m), Uvicorn
- **IA & NLP:** RAG, Hugging Face Embeddings (multilingual-e5-large), ChromaDB
- **Frontend:** React, TypeScript, Material-UI (MUI), Vite
- **Base de Datos:** SQLite (tickets), ChromaDB (vector store)
- **DevOps:** Docker, Docker Compose, Kubernetes, NGINX Ingress

#### Arquitectura del Sistema
El sistema implementa una arquitectura de microservicios con:
- Frontend React que gestiona el estado de la conversación
- Backend stateless FastAPI que responde a consultas
- Router LangChain para clasificación de intenciones
- RAG Chain para respuestas basadas en conocimiento
- Bases de datos persistentes para tickets y conocimiento vectorial

**Evidencia:** [A completar]

---

**Fin del Informe**

---

*Este informe de auditoría fue generado el [dd/mm/aaaa] por el equipo auditor y refleja el estado del sistema al momento de la evaluación.*

**Equipo Auditor:**  
Mirian Cuadros Garcia - 2021071083

