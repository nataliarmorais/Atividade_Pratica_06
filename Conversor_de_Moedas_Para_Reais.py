#Conversor de Moedas para Reais (BRL)

import requests
from datetime import datetime

def converter_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
         
        resposta = requests.get(url)
        resposta.raise_for_status() 
        
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        if chave not in dados:
            print("Código de moeda inválido ou não suportado.")
            return
        
        moeda = dados [chave]
        nome = moeda ["name"]
        cotacao = float (moeda["bid"])
        maximo = float (moeda["high"])
        minimo = float (moeda["low"])
        timestamp = int (moeda["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:M:%S")
        
        print("\n Cotação Atual:")
        print(f"Moeda: {nome}")
        print(f"Cotação atual:R$ {cotacao:.2f}")
        print(f"Valor máximo do dia R$ : {maximo:.2f}")
        print(f"Valor mínimo do dia R$ : {minimo:.2f}")
        print(f"Última atualização: {data_hora}")
        
    except requests.exceptions.RequestException as erro:
        print("Erro de conexão com a API: ",erro)
    except KeyError:
        print("Erro ao processar os dados da API.")
        
#Execução

moeda_input = input ("Digite o código da moeda estrangeira (ex: USD, EUR, GBP):").upper()
converter_moeda(moeda_input)
        
        
    