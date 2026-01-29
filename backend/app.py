from fastapi import FastAPI
from backend.routes.analyze import router as analyze_router
from backend.routes.health import router as health_router


app = FastAPI(title="Resume LLM Assistant")

@app.get("/")
def root():
    return {"message": "Welcome to the Resume LLM Assistant API"}

app.include_router(analyze_router)
app.include_router(health_router)