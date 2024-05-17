import time #Importamos o modulo "time" para usar comando de tempo, como o time.sleep()

new = False #criamos uma flag para saber se o usuario é novo
name = "isaac" #estou criando uma variavel de nome aqui provisoriamente, até implementarmos o json
def start():

    #Printamos um porquinho ASCII
    print("  __  __   ___   _  _   _  _     _     ___   ___   ___    ___  ")
    print(" |  \/  | |_ _| | \| | | || |   /_\   | __| |_ _| | _ \  / _ \ ")
    print(" | |\/| |  | |  | .` | | __ |  / _ \  | _|   | |  |   / | (_) |")
    print(" |_|  |_| |___| |_|\_| |_||_| /_/ \_\ |___| |___| |_|_\  \___/ ")
    print("                                                               ")
    print("                                        ")
    print("         /////--////                    ")
    print("       ////        ///                  ")
    print("     ,////  /////// ///                 ")
    print("     //////       /////     .%%%%%%     ")
    print("      //////////  ////*.%%%%%%%%%       ")
    print("       *///      //// (%%%%%%%%%%       ")
    print("          ///__///  %%%%%%%%%%%%%%%*    ")
    print("       %%%%%%%%%%%%%%%%%%%%%\___/%%%%   ")
    print("      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("   O/ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   ")
    print(" ´´    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%    ")
    print("         %%%%%%%%%%%%%%%%%%%%%%%%%      ")
    print("          %%%%%%%%%%%%%%%%%%%%%%%       ")
    print("          \%%%%/    ***     \%%%/       ")

    time.sleep(5) #Espera 5 segundos

    login() #Leva o usuario para o login

def login():
    global new #torna new uma variavel global
    print("Bem vindo, por favor, digite seu nome \n\n")
    name_ = input("-----> ")
    if (name_ != name):#confere se já existe um arquivo com esse nome no json
        new = True #se não existir, usuario inexistente = true
    menu() # leva o usuario para o menu

def menu():
    if (new == False):
        print("_-_-_-_-_-_Menu_-_-_-_-_-_\n"
          "1. Inserir dados\n"
          "2. Modificar dados existentes\n"
          "3. Excluir dados existentes\n"
          "4. Gerar relatórios\n"
          "0. Sair do programa\n"
          "_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    else:
        print("_-_-_-_-_-_Menu_-_-_-_-_-_\n"
            "1. Inserir dados\n"
            "0. Sair do programa\n"
            "_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    option = input("-----> ")
    match option:
        case "0":
            start()
        case "1":
            inserir()
        case "2":
            if (new == False):
                modificar()
            else:
                print("!Por favor, escolha uma opção de 0 a 4!\n\n")
                menu()
        case "3":
            if (new == False):
                excluir()
            else:
                print("!Por favor, escolha uma opção de 0 a 4!\n\n")
                menu()
        case "4":
            if (new == False):
                gerar()
            else:
                print("!Por favor, escolha uma opção de 0 a 4!\n\n")
                menu()
        case _:
            print("!Por favor, escolha uma opção de 0 a 4!\n\n")
            menu()
def inserir():
    print("_-_-_-_-_-_Inserir dados_-_-_-_-_-_\n"
          "1. Receita"
          "2. Despesa"
          "0. Menu"
          "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    option = input("-----> ")
    match option:
        case "0":
            menu()
        case "1":
            receita()
        case "2":
            despesa()
        case _:
            print("!Por favor, escolha uma opção de 0 a 2!\n\n")
            inserir()
def receita():
    global r1
    global rc1
    global rd1
    print("Por favor, digite o valor: \n\n")
    r1 = input("-----> ")
    print("_-_-_-_-_-_Informe a categoria_-_-_-_-_-_\n"
          "1. Salario"
          "2. Investimento"
          "3. Outros"
          "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    option = input("-----> ")
    match option:
        case "1":
            rc1 = 's'
        case "2":
            rc1 = 'i'
        case "3":
            rc1 = 'o'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        case _:
            print("!Por favor, escolha uma opção de 0 a 2!\n\n")
            receita()
    print("Por favor, digite a data (XX/XX/XXXX): \n\n")
    rd1 = input("-----> ")
start()
menu()