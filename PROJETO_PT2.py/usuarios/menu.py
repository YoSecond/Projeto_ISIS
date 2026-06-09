from compra.Compra import Compras_1
from usuarios.retirada import ani_ret
def usermenu(name):
    while True:
        print(f"""
===== OLA {name} ======
1 - LOJA
2 - AGENDAR RETIRADA
0 - SAIR
=========================
""")
        POSS_ESC = ['1','2','0']
        esc = input('DIGITE A OPÇÃO DESEJADA: ')
        if esc not in POSS_ESC:
            print('ESCOLHA INVALIDA!')
            continue
        elif esc == '1':
            Compras_1()
        elif esc == '2':
            ani_ret()
        elif esc == '0':
            break