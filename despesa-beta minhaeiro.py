import json

try:
    with open('despesa.json', 'r') as arquivo: # Se o arquivo existir, 
        #seu conteúdo será armazenado na variável dados.

        dados = json.load(arquivo) # Lê o conteúdo do arquivo dados.JSON na variável dados

except FileNotFoundError: # Se o arquivo não existir, inicializa com uma lista vazia

    dados = []

print("1. Alimentação")
print("2. Transporte/carro")
print("3. Habitação/moradia")
print("4. Educação")
print("5. Lazer")
print("6. Outros")

valor = input("-----> ")

despesa_alimentacao = 0
despesa_transportecarro = 0
despesa_habitacaomoradia = 0
despesa_educacao = 0
despesa_lazer = 0
despesa_outros = 0

if(valor == "1"):
    despesa_alimentacao = input("Insira um valor: ")

elif(valor == "2"):
    despesa_transportecarro = input("Insira um valor: ")

elif(valor == "3"):
    despesa_habitacaomoradia = input("Insira um valor: ")
elif(valor == "4"):
    despesa_educacao = input("Insira um valor: ")
elif(valor == "5"):
    despesa_lazer = input("Insira um valor: ")
elif(valor == "6"):
    despesa_outros = input("Insira um valor: ")
else:
    print("Opção inválida!")

dados_receita = {
    "despesaalimentacao" : despesa_alimentacao,
    "despesatransportecarro" : despesa_transportecarro,
    "despesahabitacaomoradia" : despesa_habitacaomoradia,
    "despesaeducacao" : despesa_educacao,
    "despesalazer" : despesa_lazer,
    "despesaoutros" : despesa_outros,
}

dados.append(dados_receita)

with open('despesa.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)