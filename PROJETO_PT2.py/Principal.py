from usuarios.Cadastrar_usuario import UserGenerator
from usuarios.type import TypeAcount
from usuarios.Login import login
from usuarios.type import TypeAcount
from usuarios.menu import usermenu
from usuarios.menuadm import admmenu
name = input("DIGITE SEU NOME: ").upper()
users = {'Segundo123#': {'SENHA': 'Segundo123#', 'ADM': True}}
while True:
    print(f'=== BEM VINDO {name} ===')
    print("""
1 - CRIAR CONTA
2 - LOGAR
0 - SAIR
""")
    posible_esc = ['1','2','0']
    esc = input('\ndigite a opção desejada: ')
    if esc not in posible_esc:
        print("OPÇÃO INVALIDA, TENTE NOVAMENTE!")
        continue
    if esc == '0':
        break
    elif esc == '1':
        UserGenerator(users)
        TypeAcount(users)
    elif esc == "2":
        login(users)
        if TypeAcount == "ADM":
            admmenu()
        else:
            usermenu()
