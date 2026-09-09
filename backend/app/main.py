from fastapi import FastAPI

from app.api.v1.documents import router as documents_router
from app.api.v1.sources import router as sources_router

app = FastAPI(
    title="NEXUS AI API",
    description="AI-Powered Resource Intelligence & Automation Platform",
    version="0.1.0",
)

app.include_router(
    sources_router,
    prefix="/api/v1",
)

app.include_router(
    documents_router,
    prefix="/api/v1",
)

@app.get("/")
def root():
    return {
        "name": "NEXUS AI",
        "message": "NEXUS AI API is running",
        "version": "0.1.0",
    }


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "nexus-ai-api",
    }
