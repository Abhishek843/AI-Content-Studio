from utils.prompts import PLANNER_PROMPT
from services.llm_service import generate_text

def plan(state):
    state.plan = generate_text(PLANNER_PROMPT.format(topic=state.topic))
    return state