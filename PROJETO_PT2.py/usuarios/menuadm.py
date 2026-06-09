from usuarios.Cadastro_ani import CadAnimal
from usuarios.Cadastro_prod import CadProduct
from usuarios.palntio import plantio
def admmenu(name):
    while True:
        print(f"""
===== OLA {name} ======
1 - CADASTRAR ANIMAL
2 - CADASTRAR PRODUTO
3 - RELATORIO
4 - PLANTIO
0 - SAIR
=========================
""")
        POSS_ESC = ['1','2','3','4','0']
        esc = input('DIGITE A OPÇÃO DESEJADA: ')
        if esc not in POSS_ESC:
            print('ESCOLHA INVALIDA!')
            continue
        elif esc == '1':
            CadAnimal()
        elif esc == '2':
            CadProduct()
        elif esc == '3':
            pass
        elif esc == '4':
            plantio()
        else:
            break