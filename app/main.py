from fastapi import FastAPI
from workers.task_queue import run_pipeline_task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Content Studio Running"}

@app.post("/generate")
def generate(topic: str):
    task = run_pipeline_task.delay(topic)
    return {"task_id": task.id}