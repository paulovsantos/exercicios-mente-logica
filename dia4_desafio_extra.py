valor_do_emprestimo = float(input('Digite o valor do empréstimo: '))
renda_mensal = float(input('Digite o valor da renda: '))
numero_de_parcelas = int(input('Digite o número de parcelas: '))

# emprestimo de 1000 reais
# renda mensal de 1450 reais
# valor da parcela 435 reais

if valor_do_emprestimo > 0:
    valor_das_parcelas = valor_do_emprestimo / numero_de_parcelas
    porcentagem = (valor_das_parcelas / renda_mensal) * 100
    
    if porcentagem <= 30:
        print(f'Empréstimo aprovado, {porcentagem:.0f}% de R${renda_mensal:.2f}')

    else:
        print('Empréstimo reprovado!')