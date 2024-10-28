type Task = {
    maquina: string,
    descricao: string,
    tarefas: Array<{
        descricao: string,
        detalhes: string
    }>,
    area_responsavel: string
}

const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });

const gptResponse = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
        {
            role: "user",
            content: "Descreva as máquinas e tarefas de manutenção no formato JSON."
        }
    ],
    functions: [
        {
            name: "generateMaintenanceTasks",
            parameters: {
                type: "object",
                properties: {
                    tarefas: {
                        type: "array",
                        items: {
                            type: "object",
                            properties: {
                                maquina: {
                                    type: "string"
                                },
                                descricao: {
                                    type: "string"
                                },
                                tarefas: {
                                    type: "array",
                                    items: {
                                        type: "object",
                                        properties: {
                                            descricao: { type: "string" },
                                            detalhes: { type: "string" }
                                        },
                                        required: ["descricao"]
                                    }
                                },
                                area_responsavel: {
                                    type: "string"
                                }
                            },
                            required: ["maquina", "descricao", "tarefas", "area_responsavel"]
                        }
                    }
                },
                required: ["tarefas"]
            }
        }
    ],
    function_call: { name: "generateMaintenanceTasks" }
});

const functionCall = gptResponse.choices[0].message.function_call;
const json = <{ tarefas: Task[] }>JSON.parse(functionCall.arguments);
