from utils.prompts import SCRIPT_PROMPT
from services.llm_service import generate_text

def generate_script(state):
    state.script = generate_text(SCRIPT_PROMPT.format(topic=state.topic))
    return state