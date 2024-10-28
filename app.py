import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

from taskcreator import get_json
from transcript import transcrever_audio

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads/"
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "allow_headers": "*",
            "expose_headers": "*",
            "allow_methods": "*",
        }
    },
)


# Cria o diretório de uploads, caso não exista
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


# Rota única para processar o áudio, transcrever e gerar JSON
@app.route("/processar_audio", methods=["POST"])
def processar_audio():
    if "audio" not in request.files:
        return jsonify({"error": "Nenhum arquivo de áudio encontrado"}), 400

    # Salva o arquivo de áudio temporariamente
    audio_file = request.files["audio"]
    filename = secure_filename(audio_file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    audio_file.save(file_path)

    try:
        # Transcreve o áudio para texto
        transcription_text = transcrever_audio(file_path)

        # Gera o JSON a partir do texto transcrito
        json_output = get_json(transcription_text)

        # Exclui o arquivo de áudio temporário após o processamento
        if os.path.exists(file_path):
            os.remove(file_path)

        # Retorna o JSON resultante
        return jsonify(json_output)

    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500


# Inicialização do servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

