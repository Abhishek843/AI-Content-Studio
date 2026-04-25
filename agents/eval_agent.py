from utils.prompts import EVAL_PROMPT
from services.llm_service import generate_text

def evaluate(state):
    score = generate_text(EVAL_PROMPT.format(script=state.script))

    try:
        state.score = float(score)
    except:
        state.score = 5.0

    return state