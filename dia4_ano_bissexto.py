ano = int(input('Digite o ano: '))

if ano % 4 == 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não é bissexto')

    