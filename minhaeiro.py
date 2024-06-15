import json
import os
import random
from datetime import datetime
from time import sleep

from prettytable import PrettyTable


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


arquivo_usuarios = os.path.join(os.path.dirname(__file__), 'usuarios.json')
arquivo_receitas = os.path.join(os.path.dirname(__file__), 'receitas.json')
arquivo_despesas = os.path.join(os.path.dirname(__file__), 'despesas.json')


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def logar_usuario(email, senha):
    global id_usuario, usuario_logado

    try:
        with open(arquivo_usuarios, 'r') as f:
            usuarios = json.load(f)
            arquivo = True
    except FileNotFoundError:
        arquivo = False
        print("Arquivo de usuários não encontrado!")
        print("Verifique o arquivo de usuários ou cadastre ao menos um usuário para utilizar o sistema.")
        input("\nPressione [ENTER] para retornar ao menu inicial.")
        limpar_tela()
        menu_inicial()

    usuario_logado = False
    if arquivo == True:
        for usuario in usuarios:
            if (usuario['email'] == email) and (usuario['senha'] == senha):
                id_usuario = usuario['id']
                usuario_logado = True
                print(f"\nUsuário {usuario['nome']} logado no sistema!")
                input("\nPressione [ENTER] para continuar.")
        if usuario_logado == False:
            print("\nUsuário não cadastrado ou senha incorreta!")
            input("\nPressione [ENTER] para retornar ao menu inicial.")
            limpar_tela()


def criar_usuario(nome, email, idade, senha):
    try:
        with open(arquivo_usuarios, 'r') as f:
            usuarios = json.load(f)
            existe_arquivo = True

    except FileNotFoundError:
        usuarios = []
        existe_arquivo = False

    hora_atual = datetime.now()
    segundo = hora_atual.second
    numero_aleatorio = random.randint(1, 1000)
    id_usuario_ = segundo * numero_aleatorio

    dic_usuario = {"id": id_usuario_, "nome": nome, "idade": idade, "senha": senha, "email": email}
    usuarios.append(dic_usuario)

    if existe_arquivo == True:
        with open(arquivo_usuarios, 'w') as f:
            json.dump(usuarios, f, indent=4)
    else:
        with open(arquivo_usuarios, 'x') as f:
            json.dump(usuarios, f, indent=4)


def listar_dados_usuario(usuario_id):
    with open(arquivo_usuarios, 'r') as f:
        usuarios = json.load(f)

    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            print("ID:      ", usuario['id'])
            print("Nome:    ", usuario['nome'])
            print("IDADE:   ", usuario['idade'])
            print("E-MAIL:  ", usuario['email'])
            print("SENHA:   ", usuario['senha'])
            input("Digite [ENTER] para prosseguir")
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


def adicionar_receita(usuario_id, valor_, data_, categoria_receitas_, descricao_receitas_):
    try:
        with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)
            existe_arquivo = True
    except FileNotFoundError:
        receitas = []
        existe_arquivo = False

    hora_atual = datetime.now()
    segundo = hora_atual.second
    numero_aleatorio = random.randint(1, 1000)
    transacao_ = segundo * numero_aleatorio

    dic_receitas = {"transacao": transacao_, "id": usuario_id, "valor": valor_, "data": data_,
                    "categoria": categoria_receitas_, "descricao": descricao_receitas_}
    receitas.append(dic_receitas)

    if existe_arquivo == True:
        with open(arquivo_receitas, 'w') as f:
            json.dump(receitas, f, indent=4)
    else:
        with open(arquivo_receitas, 'x') as f:
            json.dump(receitas, f, indent=4)


def verificar_receita(transacao):
    global dummy
    dummy = False
    try:
        with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)

        for receita in receitas:
            if receita['transacao'] == transacao:
                dummy = True
    except FileNotFoundError:
        print("\nArquivo com Receitas não encontrado!")
    return dummy


def listar_receitas(usuario_id):
    try:
        with open(arquivo_receitas, 'r') as f:
            receitas = json.load(f)

        global contador
        contador = 0
        table = PrettyTable()
        tabela = []

        for receita in receitas:
            if receita['id'] == usuario_id:
                contador += 1
                receita_ = [receita['transacao'], receita['valor'], receita['data'], receita['categoria'],
                            receita['descricao']]
                tabela.append(receita_)

        if contador == 0:
            print("\nReceitas não encontradas!")
            return contador
        else:
            tabela.sort(key=lambda x: x[2], reverse=True)
            table.field_names = ["TRANSAÇÃO", "VALOR (R$)", "DATA [DD-MM-YYYY]", "CATEGORIA", "DESCRIÇÃO"]
            for elemento in tabela:
                table.add_row(elemento)
            print(table)
    except FileNotFoundError:
        print("\nArquivo com Receitas não encontrado!")


def alterar_receitas(transacao_, novo_valor, nova_data, nova_categoria, nova_descricao):
    try:
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
    except FileNotFoundError:
        print("\nArquivo com Receitas não encontrado!")


def excluir_receita(transacao_):
    global contador
    contador = 0
    with open(arquivo_receitas, 'r') as f:
        receitas = json.load(f)

    for receita in receitas:
        if receita['transacao'] == transacao_:
            receitas.remove(receita)
            print("\nReceita excluído com sucesso!")
            contador = 1

    if (contador == 0):
        print("Por favor, digite uma transação valida!")

    with open(arquivo_receitas, 'w') as f:
        json.dump(receitas, f, indent=4)

    input("\nTecle [ENTER] para prosseguir")


def adicionar_despesa(usuario_id, valor_, data_, categoria_despesas_, descricao_despesas_):
    try:
        with open(arquivo_despesas, 'r') as f:
            despesas = json.load(f)
            existe_arquivo = True
    except FileNotFoundError:
        despesas = []
        existe_arquivo = False

    hora_atual = datetime.now()
    segundo = hora_atual.second
    numero_aleatorio = random.randint(1, 1000)
    transacao_ = segundo * numero_aleatorio

    dic_despesas = {"transacao": transacao_, "id": usuario_id, "valor": valor_, "data": data_,
                    "categoria": categoria_despesas_, "descricao": descricao_despesas_}
    despesas.append(dic_despesas)

    if existe_arquivo == True:
        with open(arquivo_despesas, 'w') as f:
            json.dump(despesas, f, indent=4)
    else:
        with open(arquivo_despesas, 'x') as f:
            json.dump(despesas, f, indent=4)


def verificar_despesa(transacao):
    global dummy
    dummy = False
    try:
        with open(arquivo_despesas, 'r') as f:
            despesas = json.load(f)

        for despesa in despesas:
            if despesa['transacao'] == transacao:
                dummy = True
    except FileNotFoundError:
        print("\nArquivo com Despesas não encontrado!")
    return dummy


def listar_despesas(usuario_id):
    with open(arquivo_despesas, 'r') as f:
        despesas = json.load(f)

    global contador
    contador = 0
    table = PrettyTable()
    tabela = []

    for despesa in despesas:
        if despesa['id'] == usuario_id:
            contador += 1
            despesa_ = [despesa['transacao'], despesa['valor'], despesa['data'], despesa['categoria'],
                        despesa['descricao']]
            tabela.append(despesa_)

    if contador == 0:
        print("\nDespesas não encontradas!")
        return contador
    else:
        tabela.sort(key=lambda x: x[2], reverse=True)
        table.field_names = ["TRANSAÇÃO", "VALOR (R$)", "DATA [DD-MM-YYYY]", "CATEGORIA", "DESCRIÇÃO"]
        for elemento in tabela:
            table.add_row(elemento)
        print(table)


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
    global contador
    contador = 0
    with open(arquivo_despesas, 'r') as f:
        despesas = json.load(f)

    for despesa in despesas:
        if despesa['transacao'] == transacao_:
            despesas.remove(despesa)
            print("\nDespesa excluído com sucesso!")
            contador = 1

    with open(arquivo_despesas, 'w') as f:
        json.dump(despesas, f, indent=4)

    if (contador == 0):
        print("Por favor, digite uma transação valida!")

    input("\nTecle [ENTER] para prosseguir")


def apagar_receitas_despesas(usuario_id):
    with open(arquivo_despesas, 'r') as f:
        despesas = json.load(f)

    for despesa in despesas:
        if despesa['id'] == usuario_id:
            despesas.remove(despesa)

    with open(arquivo_despesas, 'w') as f:
        json.dump(despesas, f, indent=4)

    with open(arquivo_receitas, 'r') as f:
        receitas = json.load(f)

    for receita in receitas:
        if receita['id'] == usuario_id:
            receitas.remove(receita)

    with open(arquivo_receitas, 'w') as f:
        json.dump(receitas, f, indent=4)


def categoria_receitas():
    print(" ---->>> CATEGORIA DE RECEITAS <<<---- ")
    print("          1 - SALÁRIO ")
    print("          2 - INVESTIMENTO ")
    print("          3 - OUTROS ")

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
            print(" ---->>> CATEGORIA DE RECEITAS <<<---- ")
            print("          1 - SALÁRIO ")
            print("          2 - INVESTIMENTO ")
            print("          3 - OUTROS ")
            opcao_ = input("Escolha a categoria da receita: ")

    return categoria_


def categoria_despesas():
    print(" ---->>> CATEGORIA DE DESPESAS <<<---- ")
    print("          1 - ALIMENTAÇÃO ")
    print("          2 - TRANSPORTE/CARRO ")
    print("          3 - HABITAÇÃO/MORADIA ")
    print("          4 - EDUCAÇÃO ")
    print("          5 - LAZER ")
    print("          6 - OUTROS ")

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
            print(" ---->>> CATEGORIA DE DESPESAS <<<---- ")
            print("          1 - ALIMENTAÇÃO ")
            print("          2 - TRANSPORTE/CARRO ")
            print("          3 - HABITAÇÃO/MORADIA ")
            print("          4 - EDUCAÇÃO ")
            print("          5 - LAZER ")
            print("          6 - OUTROS ")
            opcao_ = input("Escolha a categoria da despesa: ")

    return categoria_


def relatorio(opcao, usuario_id):
    match opcao:
        case '1':
            try:
                with open(arquivo_receitas, 'r') as f:
                    receitas = json.load(f)

                existe_receita = False
                valor_total = 0
                valor_salario = 0
                valor_investimento = 0
                valor_outros = 0
                for receita in receitas:
                    if (receita['id'] == usuario_id) and (receita['categoria'] == 'salario'):
                        existe_receita = True
                        valor_salario += receita['valor']
                    elif (receita['id'] == usuario_id) and (receita['categoria'] == 'investimento'):
                        existe_receita = True
                        valor_investimento += receita['valor']
                    elif (receita['id'] == usuario_id) and (receita['categoria'] == 'outros'):
                        existe_receita = True
                        valor_outros += receita['valor']

                if existe_receita == False:
                    print("\nReceitas não encontradas!")
                    input("Pressione [ENTER] para continuar")

                if existe_receita == True:
                    table = PrettyTable()
                    valor_total = valor_salario + valor_investimento + valor_outros
                    perc_salario = (valor_salario / valor_total) * 100
                    perc_investimento = (valor_investimento / valor_total) * 100
                    perc_outros = (valor_outros / valor_total) * 100
                    table.field_names = ["CATEGORIA", "TOTAL REGISTRADO POR CATEGORIA (R$)", "PERCENTUAL (%)"]
                    table.add_rows(
                        [
                            ["SALÁRIO", valor_salario, round(perc_salario, 2)],
                            ["INVESTIMENTO", valor_investimento, round(perc_investimento, 2)],
                            ["OUTROS", valor_outros, round(perc_outros, 2)],
                        ]
                    )
                    return print(table)
            except FileNotFoundError:
                print("\nArquivo com as Receitas dos usuários não encontrado!")

        case '2':
            try:
                with open(arquivo_despesas, 'r') as f:
                    despesas = json.load(f)

                existe_despesa = False
                valor_total = 0
                valor_alimentacao = 0
                valor_transporte = 0
                valor_habitacao = 0
                valor_educacao = 0
                valor_lazer = 0
                valor_outros = 0
                for despesa in despesas:
                    if (despesa['id'] == usuario_id) and (despesa['categoria'] == 'alimentacao'):
                        existe_despesa = True
                        valor_alimentacao += despesa['valor']
                    elif (despesa['id'] == usuario_id) and (despesa['categoria'] == 'transporte/carro'):
                        existe_despesa = True
                        valor_transporte += despesa['valor']
                    elif (despesa['id'] == usuario_id) and (despesa['categoria'] == 'habitacao/moradia'):
                        existe_despesa = True
                        valor_habitacao += despesa['valor']
                    elif (despesa['id'] == usuario_id) and (despesa['categoria'] == 'educacao'):
                        existe_despesa = True
                        valor_educacao += despesa['valor']
                    elif (despesa['id'] == usuario_id) and (despesa['categoria'] == 'lazer'):
                        existe_despesa = True
                        valor_lazer += despesa['valor']
                    elif (despesa['id'] == usuario_id) and (despesa['categoria'] == 'outros'):
                        existe_despesa = True
                        valor_outros += despesa['valor']

                if existe_despesa == False:
                    print("\nDespesas não encontradas!")
                    input("Pressione [ENTER] para continuar")

                if existe_despesa == True:
                    table = PrettyTable()
                    valor_total = valor_alimentacao + valor_transporte + valor_habitacao + valor_educacao + valor_lazer + valor_outros
                    perc_alimentacao = (valor_alimentacao / valor_total) * 100
                    perc_transporte = (valor_transporte / valor_total) * 100
                    perc_habitacao = (valor_habitacao / valor_total) * 100
                    perc_educacao = (valor_educacao / valor_total) * 100
                    perc_lazer = (valor_lazer / valor_total) * 100
                    perc_outros = (valor_outros / valor_total) * 100
                    table.field_names = ["CATEGORIA", "TOTAL REGISTRADO POR CATEGORIA (R$)", "PERCENTUAL (%)"]
                    table.add_rows(
                        [
                            ["ALIMENTAÇÃO", valor_alimentacao, round(perc_alimentacao, 2)],
                            ["TRANSPORTE/CARRO", valor_transporte, round(perc_transporte, 2)],
                            ["HABITAÇÃO/MORADIA", valor_habitacao, round(perc_habitacao, 2)],
                            ["EDUCAÇÃO", valor_educacao, round(perc_educacao, 2)],
                            ["LAZER", valor_lazer, round(perc_lazer, 2)],
                            ["OUTROS", valor_outros, round(perc_outros, 2)],
                        ]
                    )
                    return print(table)
            except FileNotFoundError:
                print("\nArquivo com as Despesas dos usuários não encontrado!")


def coletar_resposta(pergunta):
    while True:
        resposta = input(pergunta + " (a/b/c): ").strip().lower()
        if resposta in ['a', 'b', 'c']:
            return resposta
        else:
            print("Resposta inválida. Por favor, responda com 'a', 'b' ou 'c'.")


def determinar_perfil():
    print("Bem-vindo ao Questionário de Perfil Financeiro!\n")

    perguntas = [
        "1. O que você ganha por mês é o suficiente para arcar com seus custos?\n"
        "a) Consigo pagar as minhas despesas e guardar mais 10% dos meus ganhos;\n"
        "b) É suficiente, mas não consigo guardar nenhum valor de reserva;\n"
        "c) Não. É necessário usar todo o meu dinheiro e ainda o limite do cheque especial, caso necessário ainda peço para amigos e parentes o valor emprestado para pagar os meus gastos.\n",

        "2. Como você tem realizado o pagamento das suas despesas?\n"
        "a) Pago em dia, à vista e, em alguns casos, com bons descontos;\n"
        "b) Quase sempre pago em dia e à vista, mas quando realizo compras de alto valor, preciso fazer o parcelamento do pagamento.\n"
        "c) Preciso sempre realizar o parcelamento das minhas despesas e utilizo linhas de crédito como cheque especial, cartão de crédito e crediário para isso.\n",

        "3. Você possui alguma dívida em atraso?\n"
        "a) Não possuo dívidas.\n"
        "b) Tenho algumas dívidas, mas nenhuma se encontra em atraso;\n"
        "c) Possuo dívidas em atraso e não sei exatamente quais são.\n",

        "4. O seu orçamento financeiro é realizado periodicamente?\n"
        "a) Faço o orçamento de maneira periódica e comparo o orçado com o realizado;\n"
        "b) Somente registro o realizado de forma periódica, sem analisar os gastos obtidos;\n"
        "c) Não faço o meu orçamento financeiro.\n",

        "5. Você consegue fazer algum tipo de investimento?\n"
        "a) Utilizo mais de 10% do meu ganho em linhas de investimentos, que variam de acordo com os meus sonhos;\n"
        "b) Quando sobra dinheiro, invisto, normalmente, na poupança;\n"
        "c) Nunca sobra dinheiro para realizar investimentos.\n",

        "6. Como você planeja a sua aposentadoria?\n"
        "a) Tenho planos alternativos de previdência privada para garantir a minha segurança financeira, bem como minha contribuição para a previdência social;\n"
        "b) Contribuo para a previdência social. Sei que preciso de reserva extra, mas não consigo realizar este tipo de investimento atualmente;\n"
        "c) Não contribuo para a previdência social e nem para a privada.\n",

        "7. O que você entende sobre ser Independente Financeiramente?\n"
        "a) Que posso trabalhar por prazer e não por necessidade;\n"
        "b) Que posso ter dinheiro para viver de forma confortável com a minha família;\n"
        "c) Que posso curtir a vida intensamente sem me preocupar com os gastos futuros.\n",

        "8. Você sabe quais são os seus sonhos e objetivos de curto, médio e longo prazos?\n"
        "a) Sei quais são, quanto vão me custar e por quanto tempo terei que poupar para alcançar meus objetivos;\n"
        "b) Tenho muitos sonhos e sei quanto custam, mas não sei ainda como realizá-los;\n"
        "c) Não tenho sonhos ou, se tenho, sempre acabo deixando-os para o futuro, porque não consigo guardar dinheiro suficiente para realizá-los.\n",

        "9. Quando você decide fazer uma compra, é realizada a pesquisa de preços de forma antecipada?\n"
        "a) Sempre pesquiso antes de efetuar uma compra;\n"
        "b) Quase sempre pesquiso;\n"
        "c) Compro um produto que gosto independente de realizar pesquisa de valor.\n",

        "10. Antes de fazer uma nova prestação, você soma as que já precisa pagar no fim do mês?\n"
        "a) Não realizo compras em prestação;\n"
        "b) Sempre somo os valores antes de finalizar uma nova prestação;\n"
        "c) Verifico sempre se ainda possuo limite no cartão;\n",

        "11. Se um imprevisto alterasse a sua situação financeira, qual seria a sua reação?\n"
        "a) Faria um bom diagnóstico financeiro, registrando o que ganho e o que gasto, além dos meus investimentos e dívidas, se os tiverem;\n"
        "b) Cortaria despesas e gastos desnecessários para amenizar os baques causados pelo imprevisto;\n"
        "c) Não saberia por onde começar e teria medo de encarar a minha verdadeira situação financeira.\n",

        "12. Se a partir de hoje você não recebesse mais seu ganho, por quanto tempo você conseguiria manter seu atual padrão de vida?\n"
        "a) Conseguiria fazer tudo que faço por 5, 10 ou mais anos;\n"
        "b) Manteria meu padrão de vida por 1 a, no máximo, 4 anos;\n"
        "c) Não conseguiria me manter nem por alguns meses.\n",

        "13. Quando você decide comprar um produto, qual é a sua atitude?\n"
        "a) Planejo uma forma de investimento para compra;\n"
        "b) Parcelo dentro do meu orçamento;\n"
        "c) Compro e depois vejo como vou conseguir pagar.\n"
    ]

    pontuacao = 0

    for pergunta in perguntas:
        resposta = coletar_resposta(pergunta)

        if resposta == 'a':
            pontuacao += 10
        elif resposta == 'b':
            pontuacao += 5
        elif resposta == 'c':
            pontuacao += 0

    if pontuacao >= 95:
        perfil = "Investidor"
    elif 65 <= pontuacao <= 90:
        perfil = "Equilibrado Financeiramente"
    elif 20 <= pontuacao <= 60:
        perfil = "Endividado"
    elif pontuacao <= 15:
        perfil = "Superendividado"
    else:
        perfil = "Perfil indefinido"

    return perfil


def exibir_mensagem_perfil(perfil):
    if perfil == "Investidor":
        mensagem = (
            "Você sabe exatamente onde está sendo utilizado o seu dinheiro e as principais possibilidades de investimento "
            "\ne segurança para caso ocorra algum imprevisto, mantendo sua saúde financeira. Ser financeiramente consciente "
            "\nnão é uma tarefa fácil, exigindo disciplina e força de vontade para mudar de vida. Nunca se esqueça de que proteger "
            "\ne poupar o seu dinheiro é uma forma de realizar seus sonhos. Planeje seus sonhos de curto, médio e longo prazo para "
            "\nfacilitar a busca por seus objetivos e tenha cuidado ao realizar investimentos, buscando sempre fontes confiáveis "
            "\npara garantir que seu dinheiro esteja em boas mãos."
        )
    elif perfil == "Equilibrado Financeiramente":
        mensagem = (
            "Sua vida financeira está em um bom nível de estabilidade, mas a ausência ou o controle de dívidas não pode se tornar "
            "\num hábito. Você ainda não consolidou o costume de poupar ou investir dinheiro para obter lucros futuros. Seu equilíbrio "
            "\nde gastos pode desestabilizar-se com surpresas no futuro. Realize um diagnóstico financeiro junto com sua família, "
            "\nregistrando todas as despesas e receitas para traçar metas a curto, médio e longo prazo, visando cumprir seus sonhos "
            "\nde acordo com o tempo e o custo de cada objetivo."
        )
    elif perfil == "Endividado":
        mensagem = (
            "Seu padrão financeiro saiu um pouco dos eixos, mas isso nem sempre significa um problema. Você precisa traçar um "
            "\ndiagnóstico para saber em qual momento a sua situação financeira deu um deslize. O Minhaeiro pode te ajudar a registrar "
            "\ntodas as despesas e receitas para visualizar oportunidades de redução de gastos e equilibrar suas finanças. Foque em "
            "\naprender sobre educação financeira e entender suas alternativas para definir um plano de ação. Mantenha a calma, não "
            "\nse desanime, e mantenha o foco para passar pelos desafios com maturidade."
        )
    elif perfil == "Superendividado":
        mensagem = (
            "Este é um momento para ter calma! Apesar da sua situação atual, você acaba de encontrar uma oportunidade de recomeço. "
            "\nNão se culpe, mas tente entender as causas do superendividamento. Seja transparente com sua família sobre sua situação "
            "\nfinanceira e faça um diagnóstico para entender a gravidade do problema. Após esse período inicial, definam sonhos a curto, "
            "\nmédio e longo prazo visando a saúde financeira da família. Lembre-se: ninguém nasceu endividado ou investidor; todos nós "
            "\npodemos operar mudanças significativas em nossas vidas, e o segredo para isso está na educação financeira."
        )
    else:
        mensagem = "Perfil não reconhecido. Por favor, selecione um perfil válido."

    print(f"\nSeu perfil financeiro é: {perfil}\n")
    print(mensagem)


def menu_inicial():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print("  __  __   ___   _  _   _  _     _     ___   ___   ___    ___  ")
    print(r" |  \/  | |_ _| | \| | | || |   /_\   | __| |_ _| | _ \  / _ \ ")
    print(r" | |\/| |  | |  | .` | | __ |  / _ \  | _|   | |  |   / | (_) |")
    print(r" |_|  |_| |___| |_|\_| |_||_| /_/ \_\ |___| |___| |_|_\  \___/ ")
    print("                                                               ")
    print("                                        ")
    print(cor.AMARELO + "         /////--////                    ")
    print("       ////        ///                  ")
    print("     ,////  /////// ///                 ")
    print("     //////       /////", cor.AZUL + "     .%%%%%%     ")
    print(cor.AMARELO + "      //////////  ////*", cor.AZUL + ".%%%%%%%%%       ")
    print(cor.AMARELO + "       *///      //// ", cor.AZUL + "(%%%%%%%%%%       ")
    print(cor.AMARELO + "          ///__///", cor.AZUL + "  %%%%%%%%%%%%%%%*    ")
    print(r"       %%%%%%%%%%%%%%%%%%%%%\___/%%%%   ")
    print("      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("   O/ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   ")
    print(" ´´    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%    ")
    print("         %%%%%%%%%%%%%%%%%%%%%%%%%      ")
    print("          %%%%%%%%%%%%%%%%%%%%%%%       ")
    print(r"          \%%%%/    ***     \%%%/       " + cor.RESET)
    print(1 * "\n")
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print("          1 - LOGAR NO SISTEMA ")
    print("          2 - CRIAR USUÁRIO ")
    print("          3 - SAIR ")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def modulos():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERDE + " ---->>> MÓDULOS <<<---- ")
    print("1. MÓDULO DO USUÁRIO")
    print("2. MÓDULO DE RECEITAS")
    print("3. MÓDULO DE DESPESAS")
    print("4. MÓDULO DE RELATÓRIOS")
    print("5. VOLTAR AO MENU ANTERIOR")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def modulo_usario():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERDE + " ---->>> MÓDULO DO USUÁRIO <<<---- ")
    print("1. LISTAR DADOS DO USUÁRIO")
    print("2. MODIFICAR DADOS DO USUÁRIO")
    print("3. EXCLUIR USUÁRIO")
    print("4. DESCOBRIR PERFIL FINANCEIRO")
    print("5. VOLTAR AO MENU ANTERIOR")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def data():
    while True:
        try:
            date_str = input('Digite a sua data [DD-MM-YYYY]: ')
            date_str = datetime.strptime(date_str, "%d-%m-%Y")
            data_teste = datetime.strftime(date_str, "%d-%m-%Y")
            break
        except ValueError:
            print('Data inválida!')
    return data_teste
def idade():
    while True:
        try:
            idade_cadastro2 = int(input('Digite a sua idade: '))
            if(idade_cadastro2 <=0):
                print('Sua idade deve ser maior do que 0!')
            else:
                break
        except ValueError:
            print('Idade inválida!')
    return idade_cadastro2

def nova_idade():
    while True:
        try:
            idade_nova = int(input('Digite a sua nova idade: '))
            if(idade_nova <=0):
                print('Sua idade deve ser maior do que 0!')
            else:
                break
        except ValueError:
            print('Idade inválida!')
    return idade_nova

def modulo_receitas():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERDE + " ---->>> MÓDULO DE RECEITAS <<<---- ")
    print("1. ADICIONAR RECEITA")
    print("2. LISTAR RECEITAS DO USUÁRIO")
    print("3. MODIFICAR RECEITAS")
    print("4. EXCLUIR RECEITAS")
    print("5. VOLTAR AO MENU ANTERIOR")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def modulo_despesas():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERDE + " ---->>> MÓDULO DE DESPESAS <<<---- ")
    print("1. ADICIONAR DESPESA")
    print("2. LISTAR DESPESAS DO USUÁRIO")
    print("3. MODIFICAR DESPESAS")
    print("4. EXCLUIR DESPESAS")
    print("5. VOLTAR AO MENU ANTERIOR")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def modulo_relatório():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERDE + " ---->>> MÓDULO DO RELATÓRIOS <<<---- ")
    print("1. RELATÓRIOS DE RECEITAS")
    print("2. RELATÓRIOS DE DESPESAS")
    print("3. VOLTAR AO MENU ANTERIOR")
    print(cor.CIANO + "=" * 55 + cor.RESET)


def main():
    while True:
        menu_inicial()
        opcao_inicial = input("Escolha uma opção: ")

        match (opcao_inicial):
            case '1':
                email_ = input("\nDigite seu email cadastrado: ").lower()
                senha_ = input("Digite a senha cadastrada: ").lower()
                logar_usuario(email_, senha_)

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
                            idade_nova = nova_idade()
                            email_novo = input("Digite o novo e-mail: ")
                            senha_nova = input("Digite a nova senha: ")
                            modificar_dados_usuario(id_usuario, nome_novo, idade_nova, email_novo, senha_nova)
                        elif opcao_modulo_usuario == '3':
                            print("\nTodas as receitas e despesas do usuário serão excluídas!")
                            input("\nPressione [ENTER] para continuar")
                            apagar_receitas_despesas(id_usuario)
                            excluir_usuario(id_usuario)
                        elif opcao_modulo_usuario == '4':
                            perfil_ = determinar_perfil()
                            exibir_mensagem_perfil(perfil_)
                        elif opcao_modulo_usuario == '5':
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

                        if opcao_modulo_receitas == '1':
                            valor_receita = float(input("Digite o valor da receita: "))
                            data_receita = data()
                            categoria_receita = categoria_receitas()
                            descricao_receita = input("Digite uma descrição breve: ").lower()
                            adicionar_receita(id_usuario, valor_receita, data_receita, categoria_receita,
                                              descricao_receita)
                        elif opcao_modulo_receitas == '2':
                            listar_receitas(id_usuario)
                        elif opcao_modulo_receitas == '3':
                            input("\nPressione [ENTER] para mostrar a lista de receitas cadastradas!")
                            listar_receitas(id_usuario)
                            if (contador > 0):
                                transacao = int(input("\nDigite a nº da transação que você deseja alterar: "))
                                verificar_receita(transacao)
                                if (dummy == False):
                                    print("Por favor, digite uma transação valida!")
                                else:
                                    valor_novo = float(input("Digite o novo valor: "))
                                    data_nova = data()
                                    categoria_nova = categoria_receitas()
                                    descricao_nova = input("Digite a nova descrição: ")
                                    alterar_receitas(transacao, valor_novo, data_nova, categoria_nova, descricao_nova)
                        elif opcao_modulo_receitas == '4':
                            input("\nPressione [ENTER] para mostrar a lista de receitas cadastradas!")
                            listar_receitas(id_usuario)
                            if (contador > 0):
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
                            data_despesa = data()
                            categoria_despesa = categoria_despesas()
                            descricao_despesa = input("Digite uma descrição breve: ").lower()
                            adicionar_despesa(id_usuario, valor_despesa, data_despesa, categoria_despesa,
                                              descricao_despesa)
                        elif opcao_modulo_despesas == '2':
                            listar_despesas(id_usuario)
                        elif opcao_modulo_despesas == '3':
                            input("\nPressione [ENTER] para mostrar a lista de despesas cadastradas!")
                            listar_despesas(id_usuario)
                            if (contador > 0):
                                transacao = int(input("\nDigite a nº da transação que você deseja alterar: "))
                                verificar_despesa(transacao)
                                if (dummy == False):
                                    print("Por favor, digite uma transação valida!")
                                else:
                                    valor_novo = float(input("Digite o novo valor: "))
                                    data_nova = data()
                                    categoria_nova = categoria_despesas()
                                    descricao_nova = input("Digite a nova descrição: ")
                                    alterar_despesas(transacao, valor_novo, data_nova, categoria_nova, descricao_nova)
                        elif opcao_modulo_despesas == '4':
                            input("\nPressione [ENTER] para mostrar a lista de despesas cadastradas!")
                            listar_despesas(id_usuario)
                            if (contador > 0):
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

                        if opcao_modulo_relatorio == '1':
                            relatorio(opcao_modulo_relatorio, id_usuario)
                        elif opcao_modulo_relatorio == '2':
                            relatorio(opcao_modulo_relatorio, id_usuario)

                    elif opcao_modulo == '5':
                        input("Digite [ENTER] para retornar ao menu anterior.")
                        break
                    else:
                        print("\nOpção inválida!")
                        sleep(3)

            case '2':
                nome_cadastro = input("Digite o seu nome: ").lower()
                email_cadastro = input("Digite seu email: ").lower()
                idade_cadastro = idade()
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
