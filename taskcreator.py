from openai import OpenAI
import os

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

prompt = '''
    Identifique o título da tarefa, detalhes sobre a realização e descrição da atividade de maneira detalhada.
'''

def get_json(transcript):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system", 
                "content": prompt
            },
            {
                "role": "user", 
                "content": transcript
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "generateMaintenanceTasks",
                "schema": {
                    "type": "object",
                    "properties": {
                        "ordem-serviço": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "titulo": {"type": "string"},       
                                    "maquina": {"type": "string"},
                                    "descricao": {"type": "string"}
                                },
                                "required": ["titulo", "maquina", "descricao"]
                            }
                        },
                        "sumario": {"type": "string"}                      
                    },
                    "required": ["ordem-serviço", "sumario"]  
                }
            }
        }
    )

    return response.choices[0].message.content
