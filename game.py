import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Branca de Neve e as maçãs")
altura = 591    
largura = 985
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/fundo.jpg")
branca_de_neve = pygame.image.load("assets/brancadeneve150.png")
apple = pygame.image.load("assets/apple50.png")


def escreverTexto (pontos, perdidas):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render("Pontos:"+pontos,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    textoDisplay = fonte.render("Maças Perdidas:"+perdidas,True,branco)
    gameDisplay.blit(textoDisplay, (80,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("Game Over",True, branco)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    ironX = 500
    ironY = 400
    movimentoIronX = 0
    larguraIron = 150
    alturaIron = 270
    alturaMissile = 50
    larguraMissile = 50
    posicaoMissileX = 400
    posicaoMissileY = -240
    velocidadeMissile = 1
    pontos = 0
    pygame.mixer.music.load("assets/som.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    missileSound = pygame.mixer.Sound("assets/missile.wav")
    missileSound.set_volume(1)
    pygame.mixer.Sound.play(missileSound)

    explosaoSound = pygame.mixer.Sound("assets/morre.mp3")
    explosaoSound.set_volume(1)

    perdidas = 0

    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoIronX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoIronX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoIronX = 0
            
        if jogando:
            if posicaoMissileY > altura:
                perdidas = perdidas +1
                posicaoMissileY = -240
                posicaoMissileX = random.randint(0,largura)
                velocidadeMissile = velocidadeMissile + 1
                pygame.mixer.Sound.play(missileSound)
            else:
                posicaoMissileY =posicaoMissileY + velocidadeMissile

            if ironX + movimentoIronX >0 and ironX + movimentoIronX< largura-larguraIron:
                ironX = ironX + movimentoIronX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(branca_de_neve, (ironX,ironY))
            
            gameDisplay.blit(apple, (posicaoMissileX,posicaoMissileY))
            escreverTexto(str(pontos), str(perdidas))
            

            if perdidas > 5:
                jogando = False
                morreu()                

            pixelsXIron = list(range(ironX, ironX+larguraIron))
            pixelsYIron = list(range(ironY, ironY+alturaIron))

            pixelXMissile = list(range(posicaoMissileX, posicaoMissileX+larguraMissile))
            pixelYMissile = list(range(posicaoMissileY, posicaoMissileY+alturaMissile))

            colisaoY = len(list(set(pixelYMissile) & set(pixelsYIron) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXMissile) & set(pixelsXIron) ))
                print(colisaoX)
                if colisaoX >0:
                    pontos = pontos + 1
                    posicaoMissileY = -240
                    posicaoMissileX = random.randint(0,largura)
                    velocidadeMissile = velocidadeMissile + 1
                            



        pygameDisplay.update()
        clock.tick(60)

jogar()