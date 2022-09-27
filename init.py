def leiaInt(msg):
    while True:
        try:
            n = int (input(msg))
        except (ValueError, TypeError):
            print ('\033[31mErro: por favor, digite uma opção válida. \033[m')
            continue
        except (KeyboardInterrupt):
            print ('\n\033 [Usuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

def linha (tam = 42):
    return '-' * tam

def cabecalho (txt):
    print (linha())
    print (txt.center (42))
    print (linha())

def menu (lista):
    cabecalho ('BANCO DINHEIRO A RODO')
    c = 1 
    for item in lista:
        print (f"{c} - {item} ")
        c += 1
    print (linha()) 
    option = leiaInt ('Qual a quantia deseja sacar? (O valor mínimo é de R$10,00 e o máximo de R$600,00)\nPor favor, insira sua opção: ') 
    return option