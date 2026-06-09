def TypeAcount(users):
    tipo = ""
    while tipo != 'S' and tipo != 'N':
        tipo = input('DESEJA VIRAR ADM? (S/N) :').upper()
        if tipo != 'S' and tipo != 'N':
            print("OPÇÃO INVALIDA !")
    if tipo == 'N':
       print('OK')
    elif tipo == 'S': 
        usuario = input('DIGITE SEU USER: ')
        if usuario in users:
            users[usuario]['ADM'] = True
            print("CONTA DE ADM SALVA")
        else:
            print("TA DE SACANAGEM ? ESSE USUARO NÃO EXISTE")
