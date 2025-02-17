import random

opcoes = ['pedra', 'papel', 'tesoura']

usuario = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu: {usuario}")
print(f"O computador escolheu: {computador}")


if usuario == 'pedra' and computador == 'tesoura':
    print('Usuário ganhou')
elif usuario == 'tesoura' and computador == 'papel':
    print('Usuário ganhou')
elif usuario == 'papel' and computador == 'pedra':
    print('Usuário ganhou')

elif usuario == computador:
    print('Jogo empatado')

else:
    print('Computador ganhou')
