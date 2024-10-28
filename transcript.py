from openai import OpenAI
import os
         
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Create an api client
client = OpenAI(api_key=api_key)

# Load audio file
audio_file= open("./audio/WhatsApp Ptt 2024-10-21 at 19.29.47.ogg", "rb")

# Transcribe
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
# Print the transcribed text
print(transcription.text)

