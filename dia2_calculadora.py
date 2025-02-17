def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print('5 - Sair')

def somar(num1, num2):
    return num1 + num2
    
def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:  
        return "Erro! Divisão por zero."
    return num1 / num2

def menu():
    while True:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        while True:  
            mostrar_menu()
            opcao = input('Digite a opção: ')
            
            if opcao == '1':
                print(f'Resultado da soma: {somar(num1, num2)}')
                break  
                
            elif opcao == '2':
                print(f'Resultado da subtração: {subtrair(num1, num2)}')
                break
                
            elif opcao == '3':
                print(f'Resultado da multiplicação: {multiplicar(num1, num2)}')
                break
                
            elif opcao == '4':
                print(f'Resultado da divisão: {dividir(num1, num2)}')
                break
                
            elif opcao == "5":
                print("Saindo...")
                return 
                
            else:
                print("Opção inválida. Tente novamente.")
        
menu()


    
