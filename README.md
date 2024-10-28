# api-audio

## Introdução. 
Essa api será responsável por transcrever o áudio recebido, e interagir com a OPENAI p/ extrair informações relevantes para ajudar o técnico.

## Formato: 

```
  "ordem-serviço": [
    {
      "titulo": "Lubrificação dos Rolamentos",
      "maquina": "Linha 3",
      "descricao": "Realizar a lubrificação dos rolamentos da máquina na linha 3, utilizando o lubrificante azul código 6624. Conferir a ficha técnica para a quantidade exata a ser utilizada. Atenção aos sinais de desgaste e ao barulho reportado pelo pessoal."
    },
    {
      "titulo": "Verificação do Nível de Óleo",
      "maquina": "Desencapadora da Linha 12",
      "descricao": "Verificar o nível de óleo da desencapadora na linha 12. Conferir medições e assegurar que o nível está adequado para evitar picos de temperatura e possíveis falhas no funcionamento, conforme relatado pelo pessoal e enviado à gerência."
    },
    {
      "titulo": "Substituição do Filtro de Ar",
      "maquina": "Compressor 5",
      "descricao": "Trocar o filtro de ar do compressor 5 localizado na central. O filtro novo está disponível embaixo da bancada, providenciado anteriormente no almoxarifado. Esta tarefa está em estado crítico e não pode ser adiada."
    },
    {
      "titulo": "Inspeção da Bomba de Circulação",
      "maquina": "Compressores",
      "descricao": "Enquanto estiver trocando o filtro de ar, verificar o estado da bomba de circulação localizada no canto direito. Foi reportado que está emitindo barulhos estranhos, necessitando atenção."
    }
  ]
}
```



