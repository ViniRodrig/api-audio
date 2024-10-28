import textwrap
from openai import OpenAI
import os
         
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Create an api client
client = OpenAI(api_key=api_key)



prompt = '''
    Identifique as máquinas utilizadas, os procedimentos, a categoria (elétrica, hidraulica, mecanica), as tarefas a serem realizadas em cada maquina em específico. Por fim, sumarize as atividades.
'''

transcript = "Bom dia Oswaldo, tudo certo? Passando para a gente alinhar as coisas que ficaram pendente para a gente fazer no domingo Ficaram alguns serviços que acabaram que a gente não conseguiu tocar durante a semana Mas deixa eu explicar aqui para vocês algumas coisas que a gente tem que resolver logo, tá bom? Então conhecendo pela linha 3, eu preciso que façam a lubrificação dos rolamentos ali Essa máquina ali já está dando os sinais de desgaste já tem um certo tempo O pessoal reportou já barulho estranho nesse equipamento Então tem que botar o lubrificante correto, ele já está no estoque, aquele código lá, o azul 6624 Então já toma cuidado com isso, já faz essa lubrificação com essa máquina aí E não pode esquecer de conferir a ficha técnica dele para colocar a quantidade certa, tá? Da outra vez deu problema Então depois disso eu preciso também que vocês dêem uma verificada no nível de óleo lá da desencapadora, lá da linha 12 É um equipamento que do nada dá uns picos de temperatura lá, o pessoal já reportou, já mandou para a gerência Foi uma merda isso Então revisar mesmo as medições, ver se está tudo certo lá com o nível de óleo dela Porque se sair do óleo recompensado ela vai começar a esquentar e corre risco de parar e vai dar BO E também quem precisa dar uma olhada, lá no compressor 5 Aquele lá bem da central, o filtro de ar já passou do ponto Ele estava para ser trocado na última parada, mas ele acabou ficando para agora Então está bem crítico, então tem que fazer a substituição agora, agora no domingo já, não dá para esperar O filtro de novo eu já pechei, mandei o menino trazer lá do almoxarifado Está debaixo da bancada, só vocês pegarem e trocar também, tá? E aproveita que você está no compressor, aproveita e dá um polinho lá naquela bomba de circulação Aquela lá do canto direito, o pessoal falou que ela estava fazendo barulho Aproveita e dá uma olhadinha lá para mim, tá? Basicamente isso, qualquer coisa aí você não me avisa, tá? Porque eu estou de folga, segundamente resolve Valeu!"

#def get_json(transcript):
def get_json():
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
                              "maquina": {"type": "string"},
                              "atividade": {"type": "string"},
                              "tarefas": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "descricao": {"type": "string"},
                                    "detalhes": {"type": "string"},
                                  },
                              "required": ["descricao", "detalhes"]
                            }
                          },
                          "area_responsavel": {"type": "string"}
                        },
                        "required": ["maquina", "atividade", "tarefas", "area_responsavel"]
                      },  
                    },
                    "sumario" : {"type": "string"}
                },
                "required" : ["tarefas", "sumario"]
            }
      }
    }
    )

    return response.choices[0].message.content

print(get_json())