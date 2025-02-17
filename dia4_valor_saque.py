valor_saque = int(input("Digite o valor de saque: "))

if valor_saque >= 100:
    cedulas_100 = valor_saque // 100
    valor_saque = valor_saque % 100
    print(f'{cedulas_100} cédulas de 100')
    
if valor_saque >= 50:
    cedulas_50 = valor_saque // 50
    valor_saque = valor_saque % 50
    print(f'{cedulas_50} cédulas de 50')
    
if valor_saque >= 20:
    cedulas_20 = valor_saque // 20
    valor_saque = valor_saque % 20
    print(f'{cedulas_20} cédulas de 20')
    
if valor_saque >= 10:
    cedulas_10 = valor_saque // 10
    valor_saque = valor_saque % 10
    print(f'{cedulas_20} cédulas de 10')
    
if valor_saque >= 5:
    cedulas_5 = valor_saque // 5
    valor_saque = valor_saque % 5
    print(f'{cedulas_5} cédulas de 5')
    
if valor_saque >= 2:
    cedulas_2 = valor_saque // 2
    valor_saque = valor_saque % 2
    print(f'{cedulas_2} cédulas de 2')
    
    
    