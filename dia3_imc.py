peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)

peso_ideal = imc >= 18.5 and imc <= 24.9

print(f'IMC: {imc}')
print(f'Está dentro do peso ideal: {peso_ideal}')
