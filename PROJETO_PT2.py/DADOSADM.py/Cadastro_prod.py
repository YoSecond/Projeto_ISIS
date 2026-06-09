def CadProduct():
    products = {} 
    while True:
        product = input('DIGITE O NOME DO PRODUTO: ')
        value = float(input('DIGITE O VALOR DO PRODUTO: '))
        much = int(input('DIGITE A QUANTIDADE: '))
        products = {
            'PRODUTO': product,
            'VALOR': value,
            'QUANTIDADE': much
        }