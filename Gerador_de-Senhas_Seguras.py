import random
import string

def gerar_senha (tamanho):
    if tamanho < 4:
        return " A senha precisa ter pelo 4 caracteres."
    
    #Conjuntos de caracateres
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%^&*"

    #Garante pelo menos um de cada tipo
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    #Preenche o restante da senha
    todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha += random.choices(todos_os_caracteres, k=tamanho - 4)

    #Embaralhar a senha
    random.shuffle(senha)
    return ''.join(senha)

#Execução do programa

try:
    tamanho = int(input("Digite o tamanho da senha desejada (ex: 8, 12 , 16 ): "))
    senha_segura = gerar_senha(tamanho)
    print(f"Senha gerada: {senha_segura}")
except ValueError:
    print("Por favor, digite um número válido.")