from fastapi import FastAPI
from backend.routes.analyze import router as analyze_router
from backend.routes.health import router as health_router


app = FastAPI(title="Resume LLM Assistant")

app.include_router(analyze_router)
app.include_router(health_router)