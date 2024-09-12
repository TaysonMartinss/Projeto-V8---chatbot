from platform import system
from modelos.chatBot import ChatBot
from dotenv import load_dotenv
load_dotenv()
import os
import sys

def menu_opcoes(chatbot):
    while True:
        print("""
            ██╗░░░██╗░█████╗░░░░░██████╗░██████╗░████████╗
            ██║░░░██║██╔══██╗░░░██╔════╝░██╔══██╗╚══██╔══╝
            ╚██╗░██╔╝╚█████╔╝░░░██║░░██╗░██████╔╝░░░██║░░░
            ░╚████╔╝░██╔══██╗░░░██║░░╚██╗██╔═══╝░░░░██║░░░
            ░░╚██╔╝░░╚█████╔╝██╗╚██████╔╝██║░░░░░░░░██║░░░
            ░░░╚═╝░░░░╚════╝░╚═╝░╚═════╝░╚═╝░░░░░░░░╚═╝░░░
                """)
        print()
        print("1) nova conversa")
        print("2) Histórico")
        print("3) sair")
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                chat_app(chatbot)  # Passa o objeto chatbot como argumento
            elif opcao_escolhida == 2:
                chatbot.mostrar_historico()
            elif opcao_escolhida == 3:
                print('Até logo...')
                sys.exit(0)
            else:
                print("Opção inválida!!!")
        except ValueError:
            print("Caractere inválido!! Por favor, digite um número.")

def chat_app(chatbot):
    chatbot.start()

def main():
    api_key = os.getenv('API_KEY')
    chatbot = ChatBot(api_key)
    menu_opcoes(chatbot)

if __name__ == "__main__":
    main()
