from pydantic import BaseModel
from typing import List

class Scene(BaseModel):
    scene: str
    visual: str

class PipelineState(BaseModel):
    topic: str
    plan: str = ""
    script: str = ""
    hooks: List[str] = []
    scenes: List[Scene] = []
    images: List[str] = []
    audio: str = ""
    video: str = ""
    score: float = 0.0