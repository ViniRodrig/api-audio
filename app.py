import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from transcript import transcrever_audio
from taskcreator import get_json

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads/"

# Cria o diretório de uploads, caso não exista
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Rota única para processar o áudio, transcrever e gerar JSON
@app.route('/processar_audio', methods=['POST'])
def processar_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "Nenhum arquivo de áudio encontrado"}), 400
    
    # Salva o arquivo de áudio temporariamente
    audio_file = request.files['audio']
    filename = secure_filename(audio_file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    audio_file.save(file_path)

    try:
        # Transcreve o áudio para texto
        transcription_text = transcrever_audio(file_path)
        
        # Gera o JSON a partir do texto transcrito
        json_output = get_json(transcription_text)

        # Exclui o arquivo de áudio temporário após o processamento
        os.remove(file_path)

        # Retorna o JSON resultante
        return jsonify({"json_output": json_output})

    except Exception as e:
        os.remove(file_path)
        return jsonify({"error": str(e)}), 500

# Inicialização do servidor
if __name__ == '__main__':
    app.run(debug=True)
