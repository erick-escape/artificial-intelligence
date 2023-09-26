import pyttsx3
import time

# from elevenlabs import generate, play, set_api_key

# set_api_key("")


def act(str):
    engine = pyttsx3.init()
    engine.setProperty('voice', "brazil")
    engine.say(str)
    time.sleep(3)
    engine.runAndWait()
    time.sleep(3)
    # audio = generate(text=str, api_key="",
    #                  voice="Daniel", model="eleven_multilingual_v2")
    # play(audio)
    # time.sleep(3)
