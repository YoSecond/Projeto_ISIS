def UserGenerator(users):
    contador = 0
    while contador <= 2:
        user = input('DIGITE SEU USUARIO: ')
        password = input('DIGITE SUA SENHA: ')
        user_count = 0
        password_count = 0
        mai = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        esp = ['!','@','#','$','%','&','*','-','_','+','/','.',',']
        for u in esp:
            if u in user:
                user_count += 1
                break
        for u in mai:
            if u in user:
                user_count += 1
                break
        if len(user) >= 8:
            user_count += 1
        for i in esp:
            if i in password:
                password_count += 1
                break
        for i in mai:
            if i in password:
                password_count += 1
                break
        if len(password) >= 8:
            password_count += 1
        if user_count == 3 and password_count == 3:
            users[user] = {
                "SENHA":password,
                "ADM":False
            }
            print(users)
            break
        else:
         contador += 1
         print('USUARIO OU SENHA INVALIDOS!')
         