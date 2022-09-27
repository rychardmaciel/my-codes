from lib.interface.init import *

while True:
    option = menu (["[1] 600,00", "[2] 300,00", "[3] 100,00", "[4] Outro Valor", "[5] Sair do Sistema"])
    if option == 1:
        valor = 600
        notas100 = valor // 100
        print (f"Total de Notas de R$100,00 = ", notas100,"Notas")
        print ('-' * 42)
        print ('Volte sempre ao Banco Dinheiro a Rodo!')
        break
    elif option == 2:
        valor = 300
        notas100 = valor // 100
        print (f"Total de Notas de R$100,00 = ", notas100,"Notas")
        print ('-' * 42)
        print ('Volte sempre ao Banco Dinheiro a Rodo!')
        break
    elif option == 3:
        valor = 100
        notas100 = valor // 100
        print (f"Total de Notas de R$100,00 = ", notas100,"Nota")
        print ('-' * 42)
        print ('Volte sempre ao Banco Dinheiro a Rodo!')
        break
    elif option == 4:
        valor = int (input("Qual valor você deseja sacar? R$ "))
        notas100 = valor // 100
        resto = valor - notas100 * 100
        notas50 = resto // 50
        resto = resto - notas50 * 50
        notas20 = resto // 20
        resto = resto - notas20 * 20
        notas10 = resto // 10
        resto = resto - notas10 * 10
        notas5 = resto // 5
        resto = resto - notas5 *5
        print(f"O total de cédulas de R$ 100 é: ", notas100)
        print(f"O total de cédulas de R$ 50 é: ", notas50)
        print(f"O total de cédulas de R$ 20 é: ", notas20)
        print(f"O total de cédulas de R$ 10 é: ", notas10)
        print(f"O total de cédulas de R$ 5 é: ", notas5)
        print ('-' * 42)
        print (f'Volte sempre ao Banco Dinheiro a Rodo!')
        break
    elif option == 5:
        break
    else:
        print("Opção Inválida")
        print ('-' * 42)
        print ('Volte sempre ao Banco Dinheiro a Rodo!')
        break