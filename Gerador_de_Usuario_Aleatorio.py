# Gerador de Usuário Aleatório (com API randomuser.me)

import requests

def gerar_usuario():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        resposta.raise_for_status()
        
        dados = resposta.json()
        usuario = dados ['results'][0]
        
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("\n Usuário gerado com sucesso!")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except (KeyError, IndexError):
        print("Erro ao processar os dados da API.")
        
# Execução do programa

gerar_usuario()
   