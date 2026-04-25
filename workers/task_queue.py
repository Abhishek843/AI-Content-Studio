from celery import Celery
from graph.workflow import build_graph

celery = Celery(__name__, broker="redis://localhost:6379")

@celery.task
def run_pipeline_task(topic):
    graph = build_graph()
    return graph.invoke({"topic": topic})