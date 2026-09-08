from fastapi import FastAPI

app = FastAPI(
    title="NEXUS AI API",
    description="AI-Powered Resource Intelligence & Automation Platform",
    version="0.1.0",
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