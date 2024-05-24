import json
import os
from datetime import datetime

json_file = "receitas.json"

if not os.path.exists(json_file):
    with open(json_file, "w") as file:
        json.dump({"receitas": []}, file)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def adicionar_receita(receita):
    with open(json_file, "r") as file:
        data = json.load(file)

    data["receitas"].append(receita)

    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


def ler_receitas():
    with open(json_file, "r") as file:
        data = json.load(file)
    receitas = data["receitas"]
    return sorted(receitas, key=lambda x: datetime.strptime(x["data"], "%d/%m/%Y"))


def excluir_receita(index):
    receitas = ler_receitas()
    if 0 <= index < len(receitas):
        del receitas[index]
        with open(json_file, "w") as file:
            json.dump({"receitas": receitas}, file, indent=4)
        print("Receita excluída com sucesso!")
    else:
        print("Índice inválido!")


def inserir_receita():
    clear()
    r1 = input("Por favor, digite o valor em reais: ")
    clear()
    print("_-_-_-_-_-_Informe a categoria_-_-_-_-_-_\n"
          "1. Salario\n"
          "2. Investimento\n"
          "3. Outros\n"
          "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    option = input("Escolha uma opção: ")
    rc1 = None
    if option == "1":
        rc1 = 'Salario'
    elif option == "2":
        rc1 = 'Investimento'
    elif option == "3":
        rc1 = 'Outros'
    else:
        print("!Por favor, escolha uma opção de 1 a 3!")
        return

    clear()
    rd1 = input("Por favor, digite a data (XX/XX/XXXX): ")
    clear()
    ri1 = input("Deseja inserir uma descrição? (S/N): ")
    descricao = input("Digite a descrição: ") if ri1.lower() == "s" else None

    nova_receita = {"valor": r1, "categoria": rc1, "data": rd1, "descricao": descricao}
    adicionar_receita(nova_receita)

    print("Receita adicionada com sucesso!")


def excluir_menu():
    receitas = ler_receitas()
    print("\nReceitas:")
    for i, receita in enumerate(receitas):
        print(f"{i}. {receita['data']}: R$ {receita['valor']} - {receita['categoria']}")

    if receitas:
        index = int(input("\nDigite o número da receita que deseja excluir: "))
        excluir_receita(index)
    else:
        print("Não há receitas para excluir.")


inserir_receita()
print("\nReceitas:")
receitas = ler_receitas()
print("\nReceitas:")
for i, receita in enumerate(receitas):
    print(f"{i}. {receita['data']}: R$ {receita['valor']} - {receita['categoria']}")

excluir_menu()
print("\nReceitas atualizadas:")
receitas_atualizadas = ler_receitas()
for i, receita in receitas_atualizadas:
    print(f"{i}. {receita['data']}: R$ {receita['valor']} - {receita['categoria']}")