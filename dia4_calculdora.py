numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))
operacao = (input('Operacao (+, -, *, /): '))


if operacao == '+':
    somar = numero1 + numero2
    print(f'Soma = {somar}')
elif operacao == '-':
    subtrair = numero1 - numero2
    print(f'Subtração = {subtrair}')
elif operacao == '*':
    multiplicar = numero1 * numero2
    print(f'Multiplicação = {multiplicar}')
else:
    dividir = numero1 / numero2
    print(f'Divisão = {dividir}')