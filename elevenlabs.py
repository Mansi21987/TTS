from elevenlabs.client import ElevenLabs
from elevenlabs import generate, play

client = ElevenLabs(api_key="sk_f4932e4b9bdcc204070a7ef2da6f16710ec425a321eb0982")

# Generate audio with streaming enabled
stream = generate(
    text="I love my dog pretty much",
    voice="Jessica",
    stream=True
)

# Play the streamed audio. Ensure that the data format is correct.
play(stream)

