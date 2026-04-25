from moviepy.editor import *

def create_video(state):
    clips = []

    for img in state.images:
        clips.append(ImageClip(img).set_duration(3))

    video = concatenate_videoclips(clips)

    audio = AudioFileClip(state.audio)
    video = video.set_audio(audio)

    output = "output/final.mp4"
    video.write_videofile(output, fps=24)

    state.video = output
    return state