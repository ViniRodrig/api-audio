import requests

url = 'http://127.0.0.1:5000/processar_audio'
audio_file_path = 'audio/WhatsApp Ptt 2024-10-21 at 19.29.47.ogg'

with open(audio_file_path, 'rb') as audio_file:
    files = {'audio': audio_file}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print(response.json())
else:
    print("Erro:", response.status_code, response.text)
