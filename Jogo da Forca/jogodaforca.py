##by Leonardo Grotto e Rychard Paiva

import os
import sys
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

vitoriadesafiante = 0
vitoriacompetidor = 0

print("\nBem-Vindo ao Jogo da Forca!\n")

nomeDesafiante = input("Qual é o nome do desafiante? ")
nomeCompetidor = input("Qual é o nome do competidor? ")
palavra = input("Digite a palavra secreta:")
dica1 = input("Dica número 1: ")
dica2 = input("Dica número 2: ")
dica3 = input("Dica número 3: ")

os.system('cls')

jogar = input("Aperte a tecla ENTER do seu teclado para iniciar o Jogo da Forca! ")

digitadas = []
acertos = []
erros = 0

while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else "."
        print(senha)
        if senha == palavra:
            print("Você acertou!")
            if input('Jogar novamente? S/N: ').lower() == 'n':
                break
            elif input('Jogar novamente? S/N: ').lower() == 's': 
                restart_program()
            vitoriacompetidor =+ 1
            
       
        tentativa = input("Digite uma letra ou solicite as dicas com 1, 2 ou 3:")
        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue
        elif tentativa == '1': print ("A dica 1 e:", dica1)
        elif tentativa == '2': print ("A dica 2 e:", dica2)
        elif tentativa == '3': print ("A dica 3 e:", dica3)
        else:
            digitadas += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                print("Você errou!")
                vitoriadesafiante =+ 1
        print("X==:==\nX  :   ")
        print("X  O   " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |   "
        elif erros == 3:
            linha2 = " /|   "
        elif erros >= 4:
            linha2 = " /|\ "
        print("X%s" % linha2)
        linha3 = ""
        if erros == 5:
            linha3 += " /     "
        elif erros >= 6:
            linha3 += " / \ "
        print("X%s" % linha3)
        print("X\n===========")
        if erros == 6:
            print("Enforcado! A palavra era", palavra)
            if input('Jogar novamente? S/N: ').lower() == 'n':
                break
            elif input('Jogar novamente? S/N: ').lower() == 's': 
                restart_program()