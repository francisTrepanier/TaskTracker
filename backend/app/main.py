from fastapi import FastAPI

app = FastAPI(
    title="TaskTracker",
    version="1.0.0",
    description="Task tracker API"
)

@app.get("/")
def root():
    return {"message": "TaskTracker API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}