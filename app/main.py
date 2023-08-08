from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import compress_image_router, health_router

# criar a aplicacao
app = FastAPI()

# inclui  as rotas
app.include_router(health_router)
app.include_router(compress_image_router)
