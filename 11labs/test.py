from elevenlabs import generate, play
from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("eb23a97bf0e94745db15caa71a7fa49e")

audio = generate(
    text="Voltei",
    voice="Daniel",
    model="eleven_multilingual_v2"
)

play(audio)
