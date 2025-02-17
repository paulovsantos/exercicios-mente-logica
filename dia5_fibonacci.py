numero = int(input('Digite um número: '))

f1 = 0
f2 = 1

for _ in range(numero):
    print(f1, end=' ')
    f1, f2 = f2, f1 + f2
    