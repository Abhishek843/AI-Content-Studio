from langgraph.graph import StateGraph
from models.schema import PipelineState

from agents.planner_agent import plan
from agents.script_agent import generate_script
from agents.hook_agent import optimize_hook
from agents.scene_agent import generate_scenes
from agents.visual_agent import generate_visuals
from agents.eval_agent import evaluate

from services.image_service import generate_images
from services.tts_service import generate_audio
from services.video_service import create_video

def build_graph():
    graph = StateGraph(PipelineState)

    graph.add_node("planner", plan)
    graph.add_node("script", generate_script)
    graph.add_node("hook", optimize_hook)
    graph.add_node("scene", generate_scenes)
    graph.add_node("visual", generate_visuals)
    graph.add_node("image", generate_images)
    graph.add_node("audio", generate_audio)
    graph.add_node("video", create_video)
    graph.add_node("eval", evaluate)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "script")
    graph.add_edge("script", "hook")
    graph.add_edge("hook", "scene")
    graph.add_edge("scene", "visual")
    graph.add_edge("visual", "image")
    graph.add_edge("image", "audio")
    graph.add_edge("audio", "video")
    graph.add_edge("video", "eval")

    def should_retry(state):
        return state.score < 7

    graph.add_conditional_edges(
        "eval",
        should_retry,
        {True: "script", False: "__end__"}
    )

    return graph.compile()