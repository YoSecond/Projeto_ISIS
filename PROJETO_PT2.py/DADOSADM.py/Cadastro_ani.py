def CadAnimal():
    while True:
        animais = []
        Name = input('DIGITE O NOME DO ANIMAL: ')
        Value = float(input('DIGITE O  VALOR DO ANIMAL: '))
        Brinco = input('DIGITE O BRINCO DO ANIMAL: ')
        status = input('DIGITE O ESTADO ATUAL DO ANIMAL: ')
        animais.append(f'NOME - {Name} | VALOR - {Value} | BRINCO - {Brinco} - STATUS | {status}')
        print(animais)
CadAnimal()