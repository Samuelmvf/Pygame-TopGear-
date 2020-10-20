import pygame
from jogador import Jogador
from arvore import Arvore
from inimigo import Inimigo
import time
#iniciando pygame
pygame.init()

#CONSTANTES
W_SIZE = W_WIDTH, W_HEIGHT = 500, 600
FAIXAS = [[40, 140], [144, 244], [248, 348]]
 #Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_DARK = (232, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
GREY_DARK = (94, 94, 94)
#fonte
font_score = pygame.font.Font('freesansbold.ttf', 65)
font_gameOver = pygame.font.SysFont(None, 55)
# definindo o texto


#Definindo Sprites
    #DRAWGROUP
drawGroup = pygame.sprite.Group()
    #SPRITES
jogador = Jogador(drawGroup)
arvore1 = Arvore(drawGroup, 0)
arvore2 = Arvore(drawGroup, 1)
inimigo1 = Inimigo(drawGroup, 0)
inimigo2 = Inimigo(drawGroup, 1)

#definindo tamanho do display, nome da janela e icone
pygame.display.set_mode(W_SIZE)
display = pygame.display.get_surface()
pygame.display.set_caption('Car Racing')
pygame.display.set_icon(pygame.image.load('gameicon.png'))

#condicao para jogo continuar
gameLoop = True
#Definindo Clock
clock = pygame.time.Clock()
#Definindo dificuldade
VELOCIDADE_BASE = 100
INCREMENTADOR_PROXIMO_NIVEL = 20
#Musica
pygame.mixer.music.load('top-Gear-Soundtrack.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#functions

def desenharTela():
    #Desenhando tela
    display.fill(WHITE)
    pygame.draw.rect(display, GREEN, (0, 0, W_WIDTH, W_HEIGHT))
    pygame.draw.rect(display, WHITE, (FAIXAS[0][0], 0, FAIXAS[2][1] - FAIXAS[0][0], W_HEIGHT))
    pygame.draw.rect(display, GREY, (FAIXAS[0][0], 0, FAIXAS[0][1] - FAIXAS[0][0], W_HEIGHT))
    pygame.draw.rect(display, GREY, (FAIXAS[1][0], 0, FAIXAS[1][1] - FAIXAS[1][0], W_HEIGHT))
    pygame.draw.rect(display, GREY, (FAIXAS[2][0], 0, FAIXAS[2][1] - FAIXAS[2][0], W_HEIGHT))
    #Desenhando Carros
    drawGroup.draw(display)
    pygame.display.update()

def checarSeBateu():
    bateu = False
    if((jogador.rect.top <= inimigo1.rect.bottom and jogador.rect.top >= inimigo1.rect.top) or (jogador.rect.bottom <= inimigo1.rect.bottom and jogador.rect.bottom >= inimigo1.rect.top)):
        if(jogador.rect.right >= inimigo1.rect.left and jogador.rect.right <= inimigo1.rect.right):
            bateu = True
        if(jogador.rect.left >= inimigo1.rect.left and jogador.rect.left <= inimigo1.rect.right):
            bateu = True

    if((jogador.rect.top <= inimigo2.rect.bottom and jogador.rect.top >= inimigo2.rect.top) or (jogador.rect.bottom <= inimigo2.rect.bottom and jogador.rect.bottom >= inimigo2.rect.top)):
        if(jogador.rect.right >= inimigo2.rect.left and jogador.rect.right <= inimigo2.rect.right):
            bateu = True
        if(jogador.rect.left >= inimigo2.rect.left and jogador.rect.left <= inimigo2.rect.right):
            bateu = True

    if(bateu):
        jogador.carroPosAcidente()
        desenharTela()
    return bateu

indice = 1
score = 0
multiplicador = 1
while gameLoop:
    if score != 0:
        if score % 50 == 0:
            multiplicador = 1 + (score / 50)

    clock.tick(VELOCIDADE_BASE + (INCREMENTADOR_PROXIMO_NIVEL * multiplicador))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
            pygame.mixer.music.stop()
    keys = pygame.key.get_pressed()
    
    if(checarSeBateu()):
        text_gameOver = font_gameOver.render('GAME OVER!', True, RED_DARK)
        display.blit(text_gameOver, [120,60])

        font_custom1 = pygame.font.Font('freesansbold.ttf', 45)
        text1 = font_custom1.render("Seu score foi: " + str(score), True, BLACK)
        display.blit(text1, [40,120])

        font_custom2 = pygame.font.Font('freesansbold.ttf', 44)
        text2 = font_custom2.render("Seu score foi: " + str(score), True, WHITE)
        display.blit(text2, [47,120])

        font_custom3 = pygame.font.Font('freesansbold.ttf', 25)
        font_custom4 = pygame.font.Font('freesansbold.ttf', 24)

        text3 = font_custom3.render("Aperte R para sair", True, BLACK)
        display.blit(text3, [100,180])

        pygame.display.flip()

        controlador = True
        while controlador:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        controlador = False
                        gameLoop = False
                        pygame.quit()
    else:
        arvore1.checarFundo()
        arvore2.checarFundo()
        if(indice % 2 == 0):
            inimigo1.inverterPosicao()
            inimigo2.inverterPosicao()
        score += inimigo1.checarFundo()
        score += inimigo2.checarFundo()
        
        if keys[pygame.K_UP]:
            jogador.moverParaCima()
        if keys[pygame.K_LEFT]:
            jogador.moverParaEsquerda()
        if keys[pygame.K_RIGHT]:
            jogador.moverParaDireita()
        if keys[pygame.K_DOWN]:
            jogador.moverParaBaixo()

        desenharTela()
        text_score = font_score.render(str(score), True, BLACK)
        display.blit(text_score, [W_WIDTH - 200, 10])
        pygame.display.flip()
    
    indice = indice + 1