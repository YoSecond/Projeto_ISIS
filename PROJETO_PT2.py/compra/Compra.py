def Compras_1(products):
    while True:
        esc =  input('\nDIGITE A OPÇÃO DESEJADA: ')
        possible_esc = ['1','2','3','0']
        if esc not in possible_esc:
            print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
            continue
        if esc == "0":
            break
        elif esc == '1':
            print("===== P R O D U T O S =====")
            contador = 1
            for product in products:
                print(f'{product}')
                contador += 1
            print("============================")
        Compra = input('DIGITE A OPÇÃO DESEJADA: ')
        if Compra == '0':
                break