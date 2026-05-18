esc1 = ['1', '2', '3']
users = ['USUARIOS']
passwords = ['SENHAS']
typest = ['TIPOS']
pontos = [0]
mai = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
esp = ['!','@','#','$','%','&','*','-','_','+','/','.',',']
meeat = [
    ['ALCATRA',25.0],
    ['PICANHA',90.0],
    ['MAMINHA',40.0],
    ['LINGUIÇA DE PORCO',12.0],
    ['LINGUIÇA DE FRANGO',15.0],
    ['PEITO DE FRANGO',22.0],
    ['PATINHO',34.0],
    ['COXÃO MOLE',36.0],
    ['CHARQUE',40.0],
]

laticin = [
    ['QUEIJO QUALHO',14.0],
    ['QUEIJO MUSSARELA',15.0],
    ['QUEIJO MANTEIGA',16.0],
    ['LEITE',7.0],
    ['IOGURTE',5.0],
    ['MANTEIGA',8.0],
    ['MARGARINA',8.5],
    ['REQUEIJÃO',7.6],
    ['DOCE DE LEITE',12.5]
]

while True:

    print('''
========== SISTEMA ISIS ==========
1 - CRIAR CONTA
2 - LOGAR
3 - SAIR
==================================
''')
    esc = input('DIGITE A OPÇÃO DESEJADA: ')
    if esc not in esc1:
        print('ESCOLHA INVÁLIDA!')
    elif esc == '3':
        print('SISTEMA ENCERRADO!')
        break
    elif esc == '1':
        user_count = 0
        user = input('DIGITE SEU USUÁRIO: ')
        if len(user) >= 8:
            user_count += 1
        for u in mai:
            if u in user:
                user_count += 1
                break
        for u in esp:
            if u in user:
                user_count += 1
                break
        if user_count == 3:
            print('USUÁRIO VÁLIDO!')
        else:
            print('USUÁRIO INVÁLIDO!')
            continue
        password_count = 0
        password = input('DIGITE SUA SENHA: ')
        if len(password) >= 8:
            password_count += 1
        for p in mai:
            if p in password:
                password_count += 1
                break
        for p in esp:
            if p in password:
                password_count += 1
                break
        if password_count == 3:
            print('SENHA VÁLIDA!')
        else:
            print('SENHA INVÁLIDA!')
            continue
        print('''
1 - ADM
2 - CLIENTE
''')
        tipo_esc = input('ESCOLHA O TIPO: ')
        if tipo_esc == '1':
            tipo_user = 'ADM'
        else:
            tipo_user = 'CLIENTE'
        users.append(user)
        passwords.append(password)
        typest.append(tipo_user)
        pontos.append(0)
        print('CONTA CRIADA COM SUCESSO!')
    elif esc == '2':
        login_user = input('DIGITE SEU USUÁRIO: ')
        login_password = input('DIGITE SUA SENHA: ')
        login_ok = False
        indice_user = 0
        tipo_logado = ''
        for i in range(1, len(users)):
            if login_user == users[i] and login_password == passwords[i]:
                login_ok = True
                indice_user = i
                tipo_logado = typest[i]
                break
        if login_ok == False:
            print('LOGIN INCORRETO!')
        else:
            if tipo_logado == 'CLIENTE':
                carrinho = []
                valor_total = 0
                while True:
                    desconto = (pontos[indice_user] // 100) * 5
                    print(f'''
========= BEM VINDO {login_user} =========
1 - LOJA
2 - SISTEMA DE FIDELIDADE
0 - VOLTAR
=========================================
''')
                    comp = input('DIGITE A OPÇÃO: ')
                    if comp == '1':
                        while True:
                            print('''
================ LOJA ================
1 - CARNES
2 - LATICÍNIOS
3 - FINALIZAR COMPRA
4 - AGENDAR RETIRADA
0 - VOLTAR
======================================
''')
                            loja = input('DIGITE A OPÇÃO: ')
                            if loja == '1':
                                print('=========== CARNES ===========')
                                contador = 1
                                for item in meeat:
                                    print(contador, '-', item[0], '- R$', item[1])
                                    contador += 1
                                print('==============================')
                                while True:
                                    buy = input('DIGITE O PRODUTO: ').upper()
                                    produto_encontrado = False
                                    for item in meeat:
                                        if buy == item[0]:
                                            produto_encontrado = True
                                            carrinho.append(item[0])
                                            valor_total += item[1]
                                            print(f'{item[0]} ADICIONADO!')
                                            break
                                    if produto_encontrado == False:
                                        print('PRODUTO INEXISTENTE!')
                                        continue
                                    add = input('ADICIONAR MAIS? (Y/N): ').upper()
                                    if add == 'Y':
                                        continue
                                    else:
                                        break
                            elif loja == '2':
                                print('======== LATICÍNIOS =========')
                                contador = 1
                                for item in laticin:
                                    print(contador, '-', item[0], '- R$', item[1])
                                    contador += 1
                                print('=============================')
                                while True:
                                    buy = input('DIGITE O PRODUTO: ').upper()
                                    produto_encontrado = False
                                    for item in laticin:
                                        if buy == item[0]:
                                            produto_encontrado = True
                                            carrinho.append(item[0])
                                            valor_total += item[1]
                                            print(f'{item[0]} ADICIONADO!')
                                            break
                                    if produto_encontrado == False:
                                        print('PRODUTO INEXISTENTE!')
                                        continue
                                    add = input('ADICIONAR MAIS? (Y/N): ').upper()
                                    if add == 'Y':
                                        continue
                                    else:
                                        break
                            elif loja == '3':
                                if carrinho == []:
                                    print('CARRINHO VAZIO!')
                                    continue
                                valor_desconto = valor_total * desconto / 100
                                valor_final = valor_total - valor_desconto
                                print('=========== NOTA FISCAL ===========')
                                print('PRODUTOS:', carrinho)
                                print(f'VALOR TOTAL: R$ {valor_total:.2f}')
                                print(f'DESCONTO: {desconto}%')
                                print(f'VALOR FINAL: R$ {valor_final:.2f}')
                                print('===================================')
                                pontos[indice_user] += int(valor_total)
                                print(f'PONTOS ACUMULADOS: {pontos[indice_user]}')
                                carrinho = []
                                valor_total = 0
                            elif loja == '4':
                                animais = [(tipo,numero)]
                                if animais == [()]:
                                    print('SEM ANIMAIS CADASTRADOS PARA RETIRADA!')
                                else:
                                    contador = 1
                                    for animal in animais:
                                     print(contador, '-', animal)
                                     contador += 1
                                     ret_ani = input('QUAL ANIMAL DESEJA AGENDAR A RETIRADA?: ').upper()
                                     num_ani = input('QUAL ONUMERO DO BRINCO DO ANIMAL? : ')
                                     ani_ret == False
                                     for i in range(1, len(animais)):
                                      if ret_ani == animais[i][0] and num_ani == animais[i][1]:
                                       ani_ret = True
                                       indice_user = i
                                       break
                                      if ani_ret == False:
                                       print('ANIMAL INCORRETO OU INESISTENTE!')
                                      else:
                                         data = False
                                         data = input('DIGITE A DATA NA QUAL DESEJA REALIZAR O AGEDAMENTO nn/nn/nnnn : ')
                                         if len(data) == 10:
                                             data = True
                                             if data == True:
                                              print('AGENDAMENTO REALIZADO!')
                                              agendamento = []
                                              agendamento.append(num_ani)
                                              agendamento.append(ret_ani)
                                         else:
                                             print('DATA ERRADA!')
                                         break
                            elif loja == '0':
                                break
                            else:
                                print('OPÇÃO INVÁLIDA!')
                    elif comp == '2':
                        desconto = (pontos[indice_user] // 100) * 5
                        if desconto > 50:
                         desconto = 50
                        print('''
========== FIDELIDADE ==========
''')
                        print(f'PONTOS: {pontos[indice_user]}')
                        print(f'DESCONTO ATUAL: {desconto}%')
                        print('''
A CADA 100 PONTOS:
+5% DE DESCONTO
================================
''')
                    elif comp == '0':
                        break
                    else:
                        print('OPÇÃO INVÁLIDA!')
            elif tipo_logado == 'ADM':
                animais = []
                while True:
                    print(f'''
========== MENU ADM ==========
ADM LOGADO: {login_user}
1 - CADASTRAR ANIMAL
2 - VER ANIMAIS
3 - CADASTRAR PRODUTO
4 - VER PRODUTOS
5 - RELATÓRIO
0 - SAIR
===============================
''')
                    opcao = input('ESCOLHA: ')
                    if opcao == '1':
                        tipo = input('TIPO DO ANIMAL: ').upper()
                        numero = input('NÚMERO DO ANIMAL: ')
                        animais.append([tipo, numero])
                        print('ANIMAL CADASTRADO!')
                    elif opcao == '2':
                        if animais == []:
                            print('SEM ANIMAIS.')
                        else:
                            print('======= ANIMAIS =======')
                            contador = 1
                            for animal in animais:
                                print(contador, '-', animal)
                                contador += 1
                    elif opcao == '3':
                        tipo_produto = input(
                            'DESEJA ADICIONAR CARNE OU LATICINIO?: '
                        ).upper()
                        if tipo_produto == 'CARNE':
                            nome = input('NOME DO PRODUTO: ').upper()
                            valor = float(input('VALOR: '))
                            meeat.append([nome, valor])
                            print('CARNE CADASTRADA!')
                        elif tipo_produto == 'LATICINIO':
                            nome = input('NOME DO PRODUTO: ').upper()
                            valor = float(input('VALOR: '))
                            laticin.append([nome, valor])
                            print('LATICÍNIO CADASTRADO!')
                        else:
                            print('TIPO INVÁLIDO!')
                    elif opcao == '4':
                        print('========= CARNES =========')
                        for item in meeat:
                            print(item)
                        print('======= LATICÍNIOS =======')
                        for item in laticin:
                            print(item)
                    elif opcao == '5':
                        animais_total = len(animais)
                        carnes_total = len(meeat)
                        laticinios_total = len(laticin)
                        print('''
=========== RELATÓRIO ===========
''')
                        print(f'TOTAL DE ANIMAIS: {animais_total}')
                        print(f'TOTAL DE CARNES: {carnes_total}')
                        print(f'TOTAL DE LATICÍNIOS: {laticinios_total}')
                        print('=================================')
                    elif opcao == '0':
                        break
                    else:
                        print('OPÇÃO INVÁLIDA!')