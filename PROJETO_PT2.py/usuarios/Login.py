def login(users):
    while True:
        login_user = input('DIGITE SEU USUÁRIO: ')
        login_password = input('DIGITE SUA SENHA: ')
        if login_user in users and users[login_user]["SENHA"] == login_password:
            print("LOGIN REALIZADO !")
            return login_user
        else:
            print("LOGIN INVALIDO!")
            return False