# Este código inicia la aplicación FastAPI del backend Lubix,
# configura rutas, middleware y dependencias globales.

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.Connection import SessionLocal
from app.routers import AuthRouters, HealthRouter

import app.models

from app.middleware.AuthMiddleware import auth_middleware
from app.middleware.CorsMiddleware import setup_cors
from app.utils.seed import run_seed
from app.Config import config


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()

    if config.RUN_SEED:
        run_seed(db)

    db.close()
    yield


app = FastAPI(
    title="Lubix API",
    lifespan=lifespan
)

setup_cors(app)

app.middleware("http")(auth_middleware)

app.include_router(AuthRouters.router)
app.include_router(HealthRouter.router)