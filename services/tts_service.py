
from gtts import gTTS

def generate_audio(state):
    tts = gTTS(state.script)
    path = "output/audio.mp3"
    tts.save(path)
    state.audio = path
    return state