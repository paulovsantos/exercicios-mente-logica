import random

palpite = int(input('Digite um número: '))
numero_secreto = random.randint(1, 100)

if palpite == numero_secreto:
    print('Você acertou!')
elif palpite > numero_secreto:
    print('Seu número é maior')
else:
    print('Seu número é menor')

print(f'Número do computador: {numero_secreto}')