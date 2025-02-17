conta_a_pagar = 150
numero_de_amigos = 3

divisao_da_conta = conta_a_pagar / numero_de_amigos
divisa_exata = divisao_da_conta % 2 == 0

print(f'Valor por amigo R$: {divisao_da_conta}')
print(divisa_exata)