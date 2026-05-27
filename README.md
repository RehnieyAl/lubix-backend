# Lubix - Backend

Backend con base de datos para el proyecto **Lubix**, desarrollado por **Yeinher Algarin**.

## Descripción

Este proyecto sirve como backend para Lubix, implementando operaciones CRUD y conexión con base de datos PostgreSQL.  
Incluye autenticación, gestión de usuarios y envío de correos electrónicos utilizando FastAPI, SQLAlchemy y SMTP con Gmail.

Versión inicial: **V1.0**

## Tecnologías y herramientas

| Tecnología / Herramienta | Uso |
|--------------------------|-----|
| Python 3.14.3 | Lenguaje principal del backend |
| FastAPI | Framework para construcción de APIs (CRUD) |
| Uvicorn | Servidor ASGI para ejecutar FastAPI |
| SQLAlchemy | ORM para manejo de base de datos |
| Alembic | Migraciones y control de versiones de la base de datos |
| PostgreSQL 18.3 | Base de datos relacional |
| psycopg2-binary | Driver de conexión entre Python y PostgreSQL |
| Pydantic | Validación de datos y esquemas |
| python-jose | Manejo de autenticación y creación de tokens JWT |
| bcrypt | Encriptación de contraseñas |
| SMTP (smtplib) | Envío de correos electrónicos (verificación y recuperación de contraseña) |
| python-dotenv | Manejo de variables de entorno desde `.env` |
| Docker | Contenerización del proyecto |
| venv | Entorno virtual de Python |

## Estructura de carpetas
```text
LUBIX-BACKEND/
│
├─ app/
│  ├─ main.py             # Punto de entrada de la aplicación FastAPI
│  ├─ database/           # Configuración y conexión a PostgreSQL
│  ├─ docs/               # Documentación del proyecto
│  ├─ models/             # Modelos ORM (tablas de la base de datos)
│  ├─ routers/            # Endpoints de la API
│  ├─ schemas/            # Esquemas de entrada y salida (Pydantic)
│  ├─ services/           # Lógica de negocio
│  └─ utils/              # Utilidades (SMTP, generador de códigos, etc.)
│
├─ config.py              # Configuraciones generales desde variables de entorno
├─ main.py                # Punto de entrada alternativo del backend
├─ .env.example           # ejemplo de variable de entorno
├─ requirements.txt       # Dependencias del proyecto
├─ docker-compose.yml     # Configuración de contenedores Docker
└─ README.md              # Documentación del proyecto
```

## Instalación

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/RehnieyAl/lubix-backend.git
cd lubix-backend
```
## Instalación sin Docker

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clonar el repositorio**  
   ```bash
    git clone https://github.com/RehnieyAl/lubix-backend.git
   ```
   
2. **crear entorno virtual venv afuera de la carpeta app**
    ```bash
    python -m venv venv
    ```
3. **Activar entorno virutal - usar bash**
    ```bash
    linux/macs: source venv/bin/activate
    windows: source venv/Scripts/activate
    ```
4. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

5. **Crear variable de entorno .env con .env.example**
    ```text
    Crear archivo .env basado en .env.example
    ```
6. **Ejecutar mitgraciones**
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```
7. **Iniciar servidor backend**
    ```bash
    uvicorn app.main:app --reload
    ```
## Instalacion con docker

1. **Clonar el repositorio**  
   ```bash
    git clone https://github.com/RehnieyAl/lubix-backend.git
   ```
2. **Crear variable de entorno .env con .env.example**
    ```text
    Crear archivo .env basado en .env.example
    ```
3. **Construir y levantar contenedores**
    ```bash
    docker compose build
    docker compose up
    ```
4. **Instalar dependencias**
    ```bash
    docker compose build
    docker compose up -d
    ```
5. **Ejecutar migracion dentro del contenedor**
    ```bash
    docker compose exec backend alembic revision --autogenerate -m "initial migration"
    docker compose exec backend alembic upgrade head
    ```

6. **Iniciar servidor si no se levanta en el contenedor**
    ```bash
    docker compose exec backend uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```
## Backend hecho por Yeinher algarin

para detener los puertos usado localmente
sudo fuser -k 8000/tcp
sudo fuser -k 5433/tcp
sudo fuser -k 5432/tcp