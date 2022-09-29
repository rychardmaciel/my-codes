#by Rychard Maciel 

n = int (input ('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n**(1/2)

print ('O dobro do número {} é igual a {}.' .format(n, dobro))
print ('O triplo do número {} é igual a {}.' .format (n, triplo))
print ('A raiz quadrada de {} é igual {:.2f}.' .format (n, raiz))

print ('Deseja calcular mais algum número?')
 
while True:
    print ('[s] SIM [n] NÃO')
    opcao = str (input('Digite sua opção: ' ))
    if opcao == "s":
        n = int (input ('Digite um número: '))
        dobro = n * 2
        triplo = n * 3
        raiz = n**(1/2)
        print ('O dobro do número {} é igual a {}.' .format(n, dobro))
        print ('O triplo do número {} é igual a {}.' .format (n, triplo))
        print ('A raiz quadrada de {} é igual {:.2f}.' .format (n, raiz))
    elif opcao == "n":
        break
print ("Saindo do Sistema!")



