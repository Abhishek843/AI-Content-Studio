PLANNER_PROMPT = "Break topic into content strategy: {topic}"

SCRIPT_PROMPT = """
Create viral YouTube Shorts script:
Topic: {topic}
"""

HOOK_PROMPT = """
Rewrite hook in 3 viral ways:
{script}
"""

SCENE_PROMPT = """
Convert script into scenes JSON:
{script}
"""

EVAL_PROMPT = """
Rate script (1-10):
{script}
"""