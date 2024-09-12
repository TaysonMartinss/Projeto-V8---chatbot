import requests
import json

class ChatBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama3-8b-8192"
        self.historico = []

    def input_do_usuario(self):
        return input('\n Você : »  ')

    def envio_requisicao(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "messages": [{"role": "user", "content": message}],
            "model": self.model
        }
        response = requests.post(self.url, headers=headers, json=data)
        return response.json()

    def processando_response(self, response):
        try:
            chat_response = response['choices'][0]['message']['content']
            print("\n Chatbot: » ", chat_response)
            return chat_response
        except (KeyError, IndexError) as e:
            print("Houve um erro ao processar a resposta da API:", e)
            return None

    def atualizar_historico(self, pergunta, resposta):
        self.historico.append({"Sua Pergunta": pergunta, "Resposta da Pergunta": resposta})

    def mostrar_historico(self):
        if not self.historico:
            print("Nenhuma conversa registrada.")
        else:
            for i, entry in enumerate(self.historico, start=1):
                print(f"\nConversa {i}:")
                print(f" Pergunta: {entry['Sua Pergunta']}")
                print(f" Resposta: {entry['Resposta da Pergunta']}")

    def start(self):
        while True:
            user_input = self.input_do_usuario()
            if user_input.lower() in ["/sair", "/exit", "/quit"]:
                print("Até logo!")
                break
            response = self.envio_requisicao(user_input)
            resposta = self.processando_response(response)
            if resposta:
                self.atualizar_historico(user_input, resposta)
