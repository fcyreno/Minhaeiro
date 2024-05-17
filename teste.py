import json

arquivo = "C:/CESAR/json/usuario.json"

file_users_inexist = False
try:
    with open(arquivo, 'r') as users_:
        usuarios = json.load(users_)
except FileNotFoundError:
    usuarios = []
    file_users_inexist = True

print("Bem vindo ao MINHAEIRO!")
nome = input("Digite o seu nome: ")
email = input("Digite o seu e-mail: ")
idade = int(input("Digite a sua idade: "))
senha = input("Digite uma senha: ")
user_id = len(usuarios) + 1

user_dic = {"id": user_id, "nome": nome, "idade": idade, "senha": senha, "email": email}
usuarios.append(user_dic)

if file_users_inexist == False:
    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)
else:
    with open(arquivo, 'x') as f:
        json.dump(usuarios, f, indent=4)
