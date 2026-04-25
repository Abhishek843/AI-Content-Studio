from diffusers import StableDiffusionPipeline
import torch
import os

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
).to("cpu")

def generate_images(state):
    os.makedirs("output", exist_ok=True)
    paths = []

    for i, scene in enumerate(state.scenes[:3]):  # limit
        prompt = scene.get("visual", scene.get("scene"))
        image = pipe(prompt).images[0]

        path = f"output/img_{i}.png"
        image.save(path)
        paths.append(path)

    state.images = paths
    return state