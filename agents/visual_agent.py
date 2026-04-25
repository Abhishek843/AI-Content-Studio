def generate_visuals(state):
    for s in state.scenes:
        s["visual"] = f"cinematic, high detail: {s['scene']}"
    return state