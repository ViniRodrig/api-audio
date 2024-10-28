from openai import OpenAI
import os

api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def transcrever_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text
