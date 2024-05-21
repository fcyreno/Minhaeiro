import json
# Inicialização das variáveis de despesa
despesa_alimentacao = 0
despesa_transportecarro = 0
despesa_habitacaomoradia = 0
despesa_lazer = 0
despesa_outros = 0
despesa_educacao = 0

# Exibição do menu
print("1. Alimentação")
print("2. Transporte/carro")
print("3. Habitação/moradia")
print("4. Educação")
print("5. Lazer")
print("6. Outros")

# Escolha do usuário
valor = input("----> Escolha uma das opções: ")

# Atribuição dos valores de despesa
if valor == "1":
    despesa_alimentacao = float(input("Insira um valor: "))

    print(f"A sua despesa com alimentação é de {despesa_alimentacao} R$")

elif valor == "2":
    despesa_transportecarro = float(input("Insira um valor: "))

    print(f"A sua despesa com transporte/carro é de {despesa_transportecarro} R$")

elif valor == "3":
    despesa_habitacaomoradia = float(input("Insira um valor: "))

    print(f"A sua despesa com alimentação é de {despesa_habitacaomoradia} R$")

elif valor == "4":
    despesa_educacao = float(input("Insira um valor: "))

    print(f"A sua despesa com educação é de {despesa_educacao} R$")

elif valor == "5":

    despesa_lazer = float(input("Insira um valor: "))

    print(f"A sua despesa com lazer é de {despesa_lazer} R$")

elif valor == "6":

    despesa_outros = float(input("Insira um valor: "))

    print(f"A sua despesa outros é de {despesa_outros} R$")
else:

    print("Opção inválida!")

dados_receita = {
    "despesaalimentacao": despesa_alimentacao,
    "despesatransportecarro": despesa_transportecarro,
    "despesahabitacaomoradia": despesa_habitacaomoradia,
    "despesaeducacao": despesa_educacao,
    "despesalazer": despesa_lazer,
    "despesaoutros": despesa_outros,
}

try:
    with open('dados.json', 'r') as arquivo: # Lê o conteúdo do arquivo JSON

        dados = json.load(arquivo) # Se o arquivo existir, seu conteúdo será armazenado na variável dados.

except FileNotFoundError:
    dados = [] # Se o arquivo não existir, inicializa com uma lista vazia

proximo_usuario = len(dados) + 1

usuario_id = (f"usuario{proximo_usuario}")

dados.append({usuario_id:dados_receita})

with open('dados.json', 'w') as arquivo: # Salvar as alterações no arquivo JSON

    json.dump(dados, arquivo, indent = 4)

excluir = str(input("Deseja excluir seus dados S/N? "))

if(excluir == 'S' or 's'):

    del dados[-1]
   
with open('dados.json', 'w') as arquivo:

    json.dump(dados, arquivo, indent = 4)

'''modificar_dados = input("Deseja modificar seus dados S/N? ")

if modificar_dados == 'S':
    print("1. Alimentação")
    print("2. Transporte/carro")
    print("3. Habitação/moradia")
    print("4. Educação")
    print("5. Lazer")
    print("6. Outros")
    modificar_dados_total = int(input("---> Escolha uma das opções: "))

    if(modificar_dados_total == 1):
        valor = (input("Insira um valor: "))
        dados_receita.update({"despesaalimentacao":valor})
        print(dados_receita)
     for x in dados_receita:
            if x == 'despesaalimentacao':
                x = valor
            break
    print(valor)
        #renomear 'despesaalimentacao'[-1]
    
with open('teste.json', 'w') as arquivo:
            json.dump(dados_receita, arquivo, indent=4)'''