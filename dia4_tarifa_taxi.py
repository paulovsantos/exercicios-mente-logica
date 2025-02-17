#tarifa 4.00 reais
#0.25 centavos por km rodado

distancia_pecorrida = float(input('Digite o KM: '))

if distancia_pecorrida > 0:
    valor_total = 4 + (distancia_pecorrida * 0.25)
    print(f'Valor total da corrida R$ {valor_total:.2f}')

