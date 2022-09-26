from lib.interface.init import *
while True:
    option = menu (["[1] 600,00", "[2] 300,00", "[3] 100,00", "[4] Outro Valor", "[5] Sair do Sistema"])
    total = option 
    céd = 100
    totalcéd = 0
    if total ==1:
        total -= céd
        totalcéd + 1
    if céd == 100:
        céd = 50
    elif céd == 50:
        céd = 20
    elif céd == 20:
        céd = 10
    elif céd == 10:
        céd = 5
    elif céd == 5:
        céd = 2
    elif céd == 2:
        céd = 1
        totalcéd = 0
    if total == 0:
            break
    else: 
        if totalcéd > 0:
            print (f"Total de {totalcéd} de cédulas de R$ {céd} ")
    print ('-' * 42)
    print ('Volte sempre ao Banco Dinheiro a Rodo!')
    break