def plantio():
    terras_aradas = []
    while True:
        poss_clim = ['SECO','ENSOLARADO','FRIO','AGRADAVEL','AMENO']
        clima = input('DIGITE O CLIMA ATUAL: ').upper
        if clima not in poss_clim:
            print('NÃO É UM CLIMA VALIDO !')
            continue
        else:
            temp = float(input('DIGITE A TEMPERATURA ATUAL: '))
            estação = input('DIGITE A ESTAÇÃO ATUAL: ').upper
            if temp <= 10 and estação != ('VERÃO','OUTONO','INVERNO','PRIMAVERA'):
                print('CLIMA DESPROPICIO PARA QUALQUER PLANTIO')
            elif temp > 20 and estação == 'VERÃO':
                print('CLIMA PORPICIO PARA PLANTIO DE CENOURAS, BATATAS, RABANETES, CEBOLINHAS E ALFACE! ')
                possplant = ('CENOURAS','BATATAS','RABANETES','CEBOLINHAS','ALFACE')
                plant = input('DESEJA PLANTAR QUAL DESSES? :')
                if plant not in possplant:
                    print('NÃO É UM TEMPO PROPICIO PARA TAL PLANTIO! ')
                else:
                    print('PLANTIO EM ANDAMENTO ! ')
                    terras_aradas.append(plant)
                    print(f'PLANTIOS ATUAIS:{terras_aradas}')