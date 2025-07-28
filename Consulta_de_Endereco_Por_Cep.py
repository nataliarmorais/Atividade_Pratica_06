#Consulta de Endereço por CEP (usando ViaCEP)

import requests

def consultar_cep (cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if "erro" in dados:
            print("CEP não encontrado.Verifique se digitou corretamente")
            return
        print ("\nEndereço Encontrado:")
        print (f"CEP: {dados['cep']}")
        print (f"Logradouro: {dados['logradouro']}")
        print (f"Bairro: {dados['bairro']}")
        print (f"Cidade: {dados['localidade']}")
        print (f"Estado: {dados['uf']}")
        
    except requests.exceptions.RequestException as erro:
        print("Erro de conexão com a API:", erro)
    except KeyError:
        print("Erro ao processar os dados recebidos")
        
#Execução

cep_usuário = input ("Digite o CEP (somente os números):")
if cep_usuário.isdigit() and len(cep_usuário)== 8:
    consultar_cep(cep_usuário)
else:
    print("CEP inválido. Digite exatamente 8 números.")
    