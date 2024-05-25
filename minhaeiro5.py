#Declaração das bibliotecas
import json
import os
from datetime import datetime
from time import sleep


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

    id_usuario_ = len(usuarios) + 1 #Definindo o id do usuário

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

def excluir_usuario(usuario_id):
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


#Menu inicial do sistema
def menu_inicial():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print("  __  __   ___   _  _   _  _     _     ___   ___   ___    ___  ")
    print(r" |  \/  | |_ _| | \| | | || |   /_\   | __| |_ _| | _ \  / _ \ ")
    print(r" | |\/| |  | |  | .` | | __ |  / _ \  | _|   | |  |   / | (_) |")
    print(r" |_|  |_| |___| |_|\_| |_||_| /_/ \_\ |___| |___| |_|_\  \___/ ")
    print("                                                               ")
    print("                                        ")
    print("         /////--////                    ")
    print("       ////        ///                  ")
    print("     ,////  /////// ///                 ")
    print("     //////       /////     .%%%%%%     ")
    print("      //////////  ////*.%%%%%%%%%       ")
    print("       *///      //// (%%%%%%%%%%       ")
    print("          ///__///  %%%%%%%%%%%%%%%*    ")
    print(r"       %%%%%%%%%%%%%%%%%%%%%\___/%%%%   ")
    print("      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("   O/ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   ")
    print(" ´´    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%    ")
    print("         %%%%%%%%%%%%%%%%%%%%%%%%%      ")
    print("          %%%%%%%%%%%%%%%%%%%%%%%       ")
    print(r"          \%%%%/    ***     \%%%/       ")

    sleep(5) #Espera 5 segundos

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
    print("5. DESLOGAR")
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
    print (cor.VERDE + " ---->>> MÓDULO DE DESPESAS <<<---- ")
    print("1. ADICIONAR DESPESA")
    print("2. LISTAR DESPESAS DO USUÁRIO")
    print("3. MODIFICAR DESPESAS")
    print("4. EXCLUIR DESPESAS")
    print("5. VOLTAR AO MENU ANTERIOR")

def despesas(valor, data, descricao):
    try:
        with open(arquivo_despesas, 'r') as f:
            despesas = json.load(f)  # Carrega o conteúdo do arquivo JSON diretamente em uma lista
    except FileNotFoundError:
        despesas = []  # Inicializa a lista como vazia se o arquivo não existir
    except json.JSONDecodeError:  # Adiciona um bloco para tratar arquivos com conteúdo inválido
        despesas = []  # Inicializa a lista como vazia se o conteúdo do arquivo for inválido

    dic_despesas = {"Id": id_usuario, "valor": valor, "data": data, "descricao": descricao}
    despesas.append(dic_despesas)

    with open(arquivo_despesas, 'w') as f:
        json.dump(despesas, f, indent=4)




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
        opcao_inicial = input("\nEscolha uma opção: ")
        match(opcao_inicial):
            case '1':
                email_ = input("\nDigite seu email cadastrado: ").lower()
                senha_ = input("Digite a senha cadastrada: ").lower()
                logar_usuario(email_, senha_)

                # Entra no menu de módulos
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
                            excluir_usuario(id_usuario)
                            break
                        elif opcao_modulo_usuario == '4':
                            print("\nVoltando ao menu anterior!")
                            sleep(3)
                            limpar_tela()
                        else:
                            print("\nOpção incorreta!")
                            print("Retornando ao Menu de Módulos")
                            sleep(3)
                            limpar_tela()

                    elif opcao_modulo == '2':
                        modulo_receitas()
                        opcao_modulo_receitas = input("Escolha uma opção: ")
                        # Implementação das opções do módulo de receitas
                        break
                    elif opcao_modulo == '3':
                        modulo_despesas()
                        opcao_modulo_despesas = input("\nEscolha uma opção: ")
                        print (cor.CIANO + "=" *55 + cor.RESET)
                        print("1. Alimentação")
                        print("2. Transporte")
                        print("3. Habitação/moradia")
                        print("4. Lazer")
                        print("5. Educação")
                        print("6. Outros")
                        escolha_despesas_final = input("\n----> Escolha uma das categorias: ")
                        print (cor.CIANO + "=" *55 + cor.RESET)

                        if escolha_despesas_final == "1":
                            data_str = input("Digite a data e horário:")

                            def converter_data(data):
                                return datetime.strptime(data, "%d/%m/%Y %H:%M")

                            data_convertida = converter_data(data_str)
                            data_convertida_str = str(data_str)
                            valorteste = input("Insira um valor: ")
                            descricaoteste = input("Insira uma descrição: ")
                            despesas(valorteste, data_convertida_str, descricaoteste)

                            print("=" * 55)

                    elif opcao_modulo == '4':
                        modulo_relatorio()
                        opcao_modulo_relatorio = input("Escolha uma opção: ")
                        # Implementação das opções do módulo de relatórios
                    elif opcao_modulo == '5':
                        input("Digite [ENTER] para retornar ao menu anterior.")
                        break
                    else:
                        print("\nOpção inválida!")
                        sleep(3)

            case '2':
                nome_cadastro = input("Digite o seu nome: ").lower()
                email_cadastro = input("Digite seu email: ").lower()
                idade_cadastro = input("Digite sua idade: ").lower()
                senha_cadastro = input("Digite uma senha de cadastro: ").lower()
                criar_usuario(nome_cadastro, email_cadastro, idade_cadastro, senha_cadastro)

            case '3':
                print("Saindo do sistema!")
                sleep(3)
                limpar_tela()
                break

            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
