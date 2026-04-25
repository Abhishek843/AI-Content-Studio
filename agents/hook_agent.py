from utils.prompts import HOOK_PROMPT
from services.llm_service import generate_text

def optimize_hook(state):
    hooks = generate_text(HOOK_PROMPT.format(script=state.script))
    state.hooks = [h for h in hooks.split("\n") if h.strip()]
    return state