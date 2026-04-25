import json
from utils.prompts import SCENE_PROMPT
from services.llm_service import generate_text

def generate_scenes(state):
    res = generate_text(SCENE_PROMPT.format(script=state.script))

    try:
        state.scenes = json.loads(res)
    except:
        state.scenes = [{"scene": state.script, "visual": state.script}]

    return state