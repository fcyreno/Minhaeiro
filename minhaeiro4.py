#Declaração das bibliotecas
import os
import json
from datetime import datetime
from time import sleep
import random

#Classe para manipular a cor dos caracteres
class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'

#Definindo os arquivos JSON para armazenamento dos dados
arquivo_usuarios = os.path.join(os.path.dirname(__file__), 'usuarios.json') #Arquivo com os dados dos usuários
arquivo_receitas = os.path.join(os.path.dirname(__file__), 'receitas.json') #Arquivo com todas as receitas cadastradas
arquivo_despesas = os.path.join(os.path.dirname(__file__), 'despesas.json') #Arquivo com todas as despesas cadastradas

#Limpa tela
def limpar_tela():
    #Verifica o sistema operacional para executar o comando de limpeza de tela correto
    if os.name == 'nt':  #Para sistemas Windows
        os.system('cls')
    else:  #Para sistemas Unix/Linux/MacOS
        os.system('clear')

#Logar com um usuário cadastrado
def logar_usuario(email, senha):
    #Declaração de variáveis globais para utilização fora da função logar_usuario()
    global id_usuario, usuario_logado 
    
    #Carregando os dados dos usuários cadastrados
    try:
        with open(arquivo_usuarios, 'r') as f:
            usuarios = json.load(f)
            arquivo = True #Existe arquivo com os dados do usuário
    #Caso arquivo com dados dos usuários não seja encontrado
    except FileNotFoundError:
        arquivo = False
        print("Arquivo de usuários não encontrado!")
        print("Verifique o arquivo de usuários ou cadastre ao menos um usuário para utilizar o sistema.")
        input("\nPressione [ENTER] para retornar ao menu inicial.")
        limpar_tela()
        menu_inicial()
    
    #Processo de log-in de usuário
    usuario_logado = False #Inicializa usuario_logado como False
    if arquivo == True:
        for usuario in usuarios:
            if (usuario['email'] == email) and (usuario['senha'] == senha):
                id_usuario = usuario['id']
                usuario_logado = True #Usuario_logado só passa a ser True se log-in e senha forem encontrados na lista de usuários
                print(f"\nUsuário {usuario['nome']} logado no sistema!")
                input("\nPressione [ENTER] para continuar.")
        if usuario_logado == False:
            print("\nUsuário não cadastrado ou senha incorreta!")
            input("\nPressione [ENTER] para retornar ao menu inicial.")
            limpar_tela()

#Criar/cadastrar um usuário
def criar_usuario(nome, email, idade, senha):
    #Carrega os dados dos usuários cadastrados
    try:
        with open(arquivo_usuarios, 'r') as f:
            usuarios = json.load(f)
            existe_arquivo = True
    #Caso o arquivo com os dados dos usuários não seja encontrado (primeira execução do programa)
    except FileNotFoundError:
        usuarios = [] #É criada uma lista de usuários vazia
        existe_arquivo = False #Existência de arquivo é setado como False

    #Definindo o id do usuário (número aleatório)
    hora_atual = datetime.now()
    segundo = hora_atual.second
    numero_aleatorio = random.randint(1, 1000)
    id_usuario_ = segundo * numero_aleatorio
    
    #Inicializando o dicionário que irá receber os dados do usuário
    dic_usuario = {"id": id_usuario_, "nome": nome, "idade": idade, "senha": senha, "email": email}
    usuarios.append(dic_usuario) #Inserindo os dados do usuário no arquivo de lista de usuários

    #Inserindo os dados do usuário no arquivo JSON
    if existe_arquivo == True: #Caso exista arquivo de usuários
        with open(arquivo_usuarios, 'w') as f:
            json.dump(usuarios, f, indent=4)
    else: #Caso não exista arquivo de usuários (primeira execução do programa)
        with open(arquivo_usuarios, 'x') as f:
            json.dump(usuarios, f, indent=4)
        
#Lista os dados do usuário logado
def listar_dados_usuario(usuario_id):
    with open(arquivo_usuarios, 'r') as f:
        usuarios = json.load(f)

    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            print("\nID:      ", usuario['id'])
            print("Nome:    ", usuario['nome'])
            print("IDADE:   ", usuario['idade'])
            print("E-MAIL:  ", usuario['email'])
            print("SENHA:   ", usuario['senha'])
            input("Digite [ENTER] para prosseguir")
        else:
            print("\nUsuário não encontrado!")
            sleep(3)
            break

#Modifica os dados do usuário logado
def modificar_dados_usuario(usuario_id, novo_nome, nova_idade, novo_email, nova_senha):
    with open(arquivo_usuarios, 'r') as f:
        usuarios = json.load(f)
    
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            usuario['senha'] = nova_senha
            usuario['email'] = novo_email
            break

    with open(arquivo_usuarios, 'w') as f:
        json.dump(usuarios, f, indent=4)

    print("\nUsuário atualizado com sucesso!")
    input("\nTecle [ENTER] para prosseguir")

#Exclui o usuário logado
def excluir_usuario(usuario_id):
    global id_usuario, usuario_logado

    with open(arquivo_usuarios, 'r') as f:
        usuarios = json.load(f)
    
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuarios.remove(usuario)

    with open(arquivo_usuarios, 'w') as f:
        json.dump(usuarios, f, indent=4)
    
    print("\nUsuário excluído com sucesso!")
    id_usuario = None
    usuario_logado = False
    input("\nTecle [ENTER] para prosseguir")

#Adicionar receita do usuário logado
def adicionar_receita(usuario_id, valor_, data_, categoria_receitas_, descricao_receitas_):
    #Carrega os dados de receitas cadastradas
    try:
        with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)
            existe_arquivo = True
    #Caso o arquivo com as receitas não seja encontrado (primeira execução do programa)
    except FileNotFoundError:
        receitas = [] #É criada uma lista de receitas vazia
        existe_arquivo = False #Existência de arquivo é setado como False
    
    #Definindo o número da transação de forma aleatória
    hora_atual = datetime.now()
    segundo = hora_atual.second
    numero_aleatorio = random.randint(1, 1000)
    transacao_ = segundo * numero_aleatorio
    
    #Inicializando o dicionário que irá receber os dados de receitas
    dic_receitas = {"transacao": transacao_, "id": usuario_id, "valor": valor_, "data": data_, "categoria": categoria_receitas_, "descricao": descricao_receitas_}
    receitas.append(dic_receitas) #Inserindo os dados de receitas no arquivo de lista de receitas

    #Inserindo os dados de receitas no arquivo JSON
    if existe_arquivo == True: #Caso exista arquivo de receitas
        with open(arquivo_receitas, 'w') as f:
            json.dump(receitas, f, indent=4)
    else: #Caso não exista arquivo de receitas (primeira execução do programa)
        with open(arquivo_receitas, 'x') as f:
            json.dump(receitas, f, indent=4)

#Lista as receitas do usuário logado
def listar_receitas(usuario_id):
    with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)
 
    contador = 0
    print("=" *75)
    print("LISTA DE RECEITAS")
    print("-" *75)
    for receita in receitas:
        if receita['id'] == usuario_id:
            contador +=1
            print("*" *75)
            print(f"TRANSAÇÃO: {receita['transacao']}, VALOR: R${receita['valor']}, DATA: {receita['data']}, CATEGORIA: {receita['categoria']}, DESCRIÇÃO: {receita['descricao']}")
            print("*" *75)
            print("=" *75)
    if contador == 0:
        print("\nReceitas não encontradas!")
    
def alterar_receitas(transacao_, novo_valor, nova_data, nova_categoria, nova_descricao):
    with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)

    for receita in receitas:
        if receita['transacao'] == transacao_:
            receita['valor'] = novo_valor
            receita['data'] = nova_data
            receita['categoria'] = nova_categoria
            receita['descricao'] = nova_descricao
            break
    
    with open(arquivo_receitas, 'w') as f:
        json.dump(receitas, f, indent=4)
    print("\nReceita atualizado com sucesso!")
    input("\nTecle [ENTER] para prosseguir") 

def excluir_receita(transacao_):
    with open(arquivo_receitas, 'r') as f:
        receitas = json.load(f)
    
    for receita in receitas:
        if receita['transacao'] == transacao_:
            receitas.remove(receita)

    with open(arquivo_receitas, 'w') as f:
        json.dump(receitas, f, indent=4)

    print("\nReceita excluído com sucesso!")
    input("\nTecle [ENTER] para prosseguir")

def adicionar_despesa(usuario_id, valor_, data_, categoria_despesas_, descricao_despesas_):
    #Carrega os dados de despesas cadastradas
    try:
        with open(arquivo_despesas, 'r') as f:
            despesas = json.load(f)
            existe_arquivo = True
    #Caso o arquivo com as despesas não seja encontrado (primeira execução do programa)
    except FileNotFoundError:
        despesas = [] #É criada uma lista de despesas vazia
        existe_arquivo = False #Existência de arquivo é setado como False
    
    #Definindo o número da transação de forma aleatória
    hora_atual = datetime.now()
    segundo = hora_atual.second
    numero_aleatorio = random.randint(1, 1000)
    transacao_ = segundo * numero_aleatorio
    
    #Inicializando o dicionário que irá receber os dados de despesas
    dic_despesas = {"transacao": transacao_, "id": usuario_id, "valor": valor_, "data": data_, "categoria": categoria_despesas_, "descricao": descricao_despesas_}
    despesas.append(dic_despesas) #Inserindo os dados de receitas no arquivo de lista de receitas

    #Inserindo os dados de despesas no arquivo JSON
    if existe_arquivo == True: #Caso exista arquivo de despesas
        with open(arquivo_despesas, 'w') as f:
            json.dump(despesas, f, indent=4)
    else: #Caso não exista arquivo de despesas (primeira execução do programa)
        with open(arquivo_despesas, 'x') as f:
            json.dump(despesas, f, indent=4)

def listar_despesas(usuario_id):
    with open(arquivo_despesas, 'r') as f:
            despesas = json.load(f)
 
    contador = 0
    print("=" *75)
    print("LISTA DE DESPESAS")
    print("-" *75)
    for despesa in despesas:
        if despesa['id'] == usuario_id:
            contador +=1
            print("*" *75)
            print(f"TRANSAÇÃO: {despesa['transacao']}, VALOR: R${despesa['valor']}, DATA: {despesa['data']}, CATEGORIA: {despesa['categoria']}, DESCRIÇÃO: {despesa['descricao']}")
            print("*" *75)
            print("=" *75)
    if contador == 0:
        print("Despesas não encontradas!")
    
def alterar_despesas(transacao_, novo_valor, nova_data, nova_categoria, nova_descricao):
    with open(arquivo_despesas, 'r') as f:
            despesas = json.load(f)

    for despesa in despesas:
        if despesa['transacao'] == transacao_:
            despesa['valor'] = novo_valor
            despesa['data'] = nova_data
            despesa['categoria'] = nova_categoria
            despesa['descricao'] = nova_descricao
            break
    
    with open(arquivo_despesas, 'w') as f:
        json.dump(despesas, f, indent=4)
    print("\nDespesa atualizado com sucesso!")
    input("\nTecle [ENTER] para prosseguir") 

def excluir_despesa(transacao_):
    with open(arquivo_despesas, 'r') as f:
        despesas = json.load(f)
    
    for despesa in despesas:
        if despesas['transacao'] == transacao_:
            despesas.remove(despesa)

    with open(arquivo_despesas, 'w') as f:
        json.dump(despesas, f, indent=4)
    print("\nDespesa excluído com sucesso!")
    input("\nTecle [ENTER] para prosseguir")

#Função que exclui todas as receitas e despesas de um usuário. Utilizada para quando um usuário específico for excluído
def apagar_receitas_despesas(usuario_id):
    #Rotina de exclusão de despesas
    with open(arquivo_despesas, 'r') as f:
        despesas = json.load(f)
    
    for despesa in despesas:
        if despesa['id'] == usuario_id:
            despesas.remove(despesa)
    
    with open(arquivo_despesas, 'w') as f:
        json.dump(despesas, f, indent=4)
    
    #Rotina de exclusão de receitas
    with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)

    for receita in receitas:
        if receita['id'] == usuario_id:
            receitas.remove(receita)
    
    with open(arquivo_receitas, 'w') as f:
        json.dump(receitas, f, indent=4)

def categoria_receitas():
    print (" ---->>> CATEGORIA DE RECEITAS <<<---- ")
    print ("          1 - SALÁRIO ")
    print ("          2 - INVESTIMENTO ")
    print ("          3 - OUTROS ")

    opcao_ = input("Escolha a categoria da receita: ")

    while True:
        if opcao_ == '1':
            categoria_ = "salario"
            break
        elif opcao_ == '2':
            categoria_ = "investimento"
            break
        elif opcao_ == '3':
            categoria_ = 'outros'
            break
        else:
            print("\nOpção inválida!")
            print (" ---->>> CATEGORIA DE RECEITAS <<<---- ")
            print ("          1 - SALÁRIO ")
            print ("          2 - INVESTIMENTO ")
            print ("          3 - OUTROS ")
            opcao_ = input("Escolha a categoria da receita: ")

    return categoria_

def categoria_despesas():
    print (" ---->>> CATEGORIA DE DESPESAS <<<---- ")
    print ("          1 - ALIMENTAÇÃO ")
    print ("          2 - TRANSPORTE/CARRO ")
    print ("          3 - HABITAÇÃO/MORADIA ")
    print ("          4 - EDUCAÇÃO ")
    print ("          5 - LAZER ")
    print ("          6 - OUTROS ")

    opcao_ = input("Escolha a categoria da despesa: ")

    while True:
        if opcao_ == '1':
            categoria_ = "alimentacao"
            break
        elif opcao_ == '2':
            categoria_ = "transporte/carro"
            break
        elif opcao_ == '3':
            categoria_ = "habitacao/moradia"
            break
        elif opcao_ == '4':
            categoria_ = "educacao"
            break
        elif opcao_ == '5':
            categoria_ = "lazer"
            break
        elif opcao_ == '6':
            categoria_ = "outros"
            break
        else:
            print (" ---->>> CATEGORIA DE DESPESAS <<<---- ")
            print ("          1 - ALIMENTAÇÃO ")
            print ("          2 - TRANSPORTE/CARRO ")
            print ("          3 - HABITAÇÃO/MORADIA ")
            print ("          4 - EDUCAÇÃO ")
            print ("          5 - LAZER ")
            print ("          6 - OUTROS ")
            opcao_ = input("Escolha a categoria da despesa: ")

    return categoria_

#Menu inicial do sistema
def menu_inicial():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERDE + " ---->>> BEM VINDO AO MINHAEIRO <<<---- ")
    print ("          1 - LOGAR NO SISTEMA ")
    print ("          2 - CRIAR USUÁRIO ")
    print ("          3 - SAIR ")
    print (cor.CIANO + "=" *55 + cor.RESET)

def modulos():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERDE + " ---->>> MÓDULOS <<<---- ")
    print("1. MÓDULO DO USUÁRIO")
    print("2. MÓDULO DE RECEITAS")
    print("3. MÓDULO DE DESPESAS")
    print("4. MÓDULO DE RELATÓRIOS")
    print("5. VOLTAR AO MENU ANTERIOR")
    print (cor.CIANO + "=" *55 + cor.RESET)

#Menu do usuário
def modulo_usario():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERDE + " ---->>> MÓDULO DO USUÁRIO <<<---- ")
    print("1. LISTAR DADOS DO USUÁRIO")
    print("2. MODIFICAR DADOS DO USUÁRIO")
    print("3. EXCLUIR USUÁRIO")
    print("4. VOLTAR AO MENU ANTERIOR")
    print (cor.CIANO + "=" *55 + cor.RESET)

def modulo_receitas():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERDE + " ---->>> MÓDULO DE RECEITAS <<<---- ")
    print("1. ADICIONAR RECEITA")
    print("2. LISTAR RECEITAS DO USUÁRIO")
    print("3. MODIFICAR RECEITAS")
    print("4. EXCLUIR RECEITAS")
    print("5. VOLTAR AO MENU ANTERIOR")
    print (cor.CIANO + "=" *55 + cor.RESET)

def modulo_despesas():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERDE + " ---->>> MÓDULO DE DESPESAS <<<---- ")
    print("1. ADICIONAR DESPESA")
    print("2. LISTAR DESPESAS DO USUÁRIO")
    print("3. MODIFICAR DESPESAS")
    print("4. EXCLUIR DESPESAS")
    print("5. VOLTAR AO MENU ANTERIOR")
    print (cor.CIANO + "=" *55 + cor.RESET)

def modulo_relatório():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERDE + " ---->>> MÓDULO DO USUÁRIO <<<---- ")
    print("1. ADICIONAR DESPESA")
    print("2. LISTAR DESPESA")
    print("3. ATUALIZAR DESPESA")
    print("4. EXCLUIR DESPESA")
    print("5. LISTAR DESPESAS DE UM USUARIO")
    print("6. VOLTAR AO MENU ANTERIOR")
    print (cor.CIANO + "=" *55 + cor.RESET)

def main():
    while True:
        menu_inicial()
        opcao_inicial = input("Escolha uma opção: ")

        match(opcao_inicial):
            case '1':
                email_ = input("\nDigite seu email cadastrado: ").lower()
                senha_ = input("Digite a senha cadastrada: ").lower()
                logar_usuario(email_, senha_)

                #Entra no menu de módulos
                while usuario_logado == True:
                    modulos()
                    opcao_modulo = input("Escolha uma opção: ")

                    if opcao_modulo == '1':
                        modulo_usario()
                        opcao_modulo_usuario = input("Escolha uma opção: ")

                        if opcao_modulo_usuario == '1':
                            listar_dados_usuario(id_usuario)
                        elif opcao_modulo_usuario == '2':
                            nome_novo = input("Digite o novo nome: ")
                            idade_nova = input("Digite a nova idade: ")
                            email_novo = input("Digite o novo e-mail: ")
                            senha_nova = input("Digite a nova senha: ")
                            modificar_dados_usuario(id_usuario, nome_novo, idade_nova, email_novo, senha_nova)
                        elif opcao_modulo_usuario == '3':
                            print("\nTodas as receitas e despesas do usuário serão excluídas!")
                            input("\nPressione [ENTER] para continuar")
                            apagar_receitas_despesas(id_usuario)
                            excluir_usuario(id_usuario)
                        elif opcao_modulo_usuario == '4':
                            print("\nVoltando ao menu anterior!")
                            sleep(3)
                            limpar_tela()
                        else:
                            print("\nOpção incorreta!")
                            print("Retornando ao Menu de Módulos")
                            sleep(3)
                            limpar_tela()

                    elif opcao_modulo =='2':
                        modulo_receitas()
                        opcao_modulo_receitas = input("Escolha uma opção: ")

                        if opcao_modulo_receitas == '1':
                            valor_receita = float(input("Digite o valor da receita: "))
                            data_receita = input("Informe a data da receita padrão [AAAA-MM-DD]: ")
                            categoria_receita = categoria_receitas()
                            descricao_receita = input("Digite uma descrição breve: ").lower()
                            adicionar_receita(id_usuario, valor_receita, data_receita, categoria_receita, descricao_receita)
                        elif opcao_modulo_receitas == '2':
                            listar_receitas(id_usuario)
                        elif opcao_modulo_receitas == '3':
                            input("\nPressione [ENTER] para mostrar a lista de receitas cadastradas!")
                            listar_receitas(id_usuario)
                            transacao = int(input("\nDigite a nº da transação que você deseja alterar: "))
                            valor_novo = float(input("Digite o novo valor: "))
                            data_nova = input("Digite a nova data padrão [AAAA-MM-DD]: ")
                            categoria_nova = categoria_receitas()
                            descricao_nova = input("Digite a nova descrição: ")
                            alterar_receitas(transacao, valor_novo, data_nova, categoria_nova, descricao_nova)
                        elif opcao_modulo_receitas == '4':
                            input("\nPressione [ENTER] para mostrar a lista de receitas cadastradas!")
                            listar_receitas(id_usuario)
                            transacao = int(input("\nDigite a nº da transação que você deseja excluir: "))
                            excluir_receita(transacao)
                        elif opcao_modulo_receitas == '5':
                            print("\nVoltando ao menu anterior!")
                            sleep(3)
                            limpar_tela()
                        else:
                            print("\nOpção incorreta!")
                            print("Retornando ao Menu de Módulos")
                            sleep(3)
                            limpar_tela()

                    elif opcao_modulo == '3':
                        modulo_despesas()
                        opcao_modulo_despesas = input("Escolha uma opção: ")
                        
                        if opcao_modulo_despesas == '1':
                            valor_despesa = float(input("Digite o valor da despesa: "))
                            data_despesa = input("Informe a data da despesa padrão [AAAA-MM-DD]: ")
                            categoria_despesa = categoria_despesas()
                            descricao_despesa = input("Digite uma descrição breve: ").lower()
                            adicionar_despesa(id_usuario, valor_despesa, data_despesa, categoria_despesa, descricao_despesa)
                        elif opcao_modulo_despesas == '2':
                            listar_despesas(id_usuario)
                        elif opcao_modulo_despesas == '3':
                            input("\nPressione [ENTER] para mostrar a lista de despesass cadastradas!")
                            listar_despesas(id_usuario)
                            transacao = int(input("\nDigite a nº da transação que você deseja alterar: "))
                            valor_novo = float(input("Digite o novo valor: "))
                            data_nova = input("Digite a nova data padrão [AAAA-MM-DD]: ")
                            categoria_nova = categoria_despesas()
                            descricao_nova = input("Digite a nova descrição: ")
                            alterar_despesas(transacao, valor_novo, data_nova, categoria_nova, descricao_nova)
                        elif opcao_modulo_despesas == '4':
                            input("\nPressione [ENTER] para mostrar a lista de despesas cadastradas!")
                            listar_despesas(id_usuario)
                            transacao = int(input("\nDigite a nº da transação que você deseja excluir: "))
                            excluir_despesa(transacao)
                        elif opcao_modulo_despesas == '5':
                            print("\nVoltando ao menu anterior!")
                            sleep(3)
                            limpar_tela()
                        else:
                            print("\nOpção incorreta!")
                            print("Retornando ao Menu de Módulos")
                            sleep(3)
                            limpar_tela()

                    elif opcao_modulo == '4':
                        modulo_relatório()
                        opcao_modulo_relatorio = input("Escolha uma opção: ")
                    elif opcao_modulo == '5':
                        input("Digite [ENTER] para retornar ao menu anterior.")
                        break
                    else:
                        print("\nOpção inválida!")
                        sleep(3)
         
            case '2':
                nome_cadastro = input("Digite o seu nome: ").lower()
                email_cadastro = input("Digite seu email: ").lower()
                idade_cadastro = input("Digite seua idade: ").lower()
                senha_cadastro = input("Digite uma senha de cadastro: ").lower()
                criar_usuario(nome_cadastro, email_cadastro, idade_cadastro, senha_cadastro)
            
            case '3':
                print("Saindo do sistema!")
                sleep(3)
                break
            
            case __:
                print("Opção inválida. Tente novamente.")
                
if __name__ == "__main__":
    main()