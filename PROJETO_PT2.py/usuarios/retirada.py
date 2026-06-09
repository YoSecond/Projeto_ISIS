def ani_ret(animais):
    while True:
        animais = []
        agendamentos = {
            'DATAS': datas,
            'HORARIOS': horario
        }
        datas = input('DIGITE A DTA PARA RETIRADA (DD/MM/AAAA) : ')
        if len(datas) < 10:
            print('DATA INVALIDA!')
            continue
        else:
            horario = input('DIGITE O HORARIO PARA RETIRADA (HH/MM): ')
            if len(horario) < 5:
                print('HORARIO INVALIDO! ')
            else:
                agendamentos[datas] = horario
                print('AGENDAMENTO REALIZADO COM SUSCEÇO!')