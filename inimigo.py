import pygame
import random
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, grupo,id):
        super().__init__(grupo)
        self.id = id
        self.image = (pygame.image.load('blue_car.png') if id == 0 else pygame.image.load('red_car.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (250, -20)
        self.allPositions = [40,193,295] if id == 0 else [91,244,142]
        self.rect.x = self.allPositions[self.id]
    
    def movimentarCarro(self):
        if(self.id == 0):
            self.rect.move_ip([0,1])
        else:
            self.rect.move_ip([0,2])            
    
    def getPosicaoRandom(self):
        return random.randint(40,298)
    
    def checarFundo(self):
        if(self.rect.y <= 600):
            self.movimentarCarro()
            return 0
        else:
            self.resetarPosicaoCarro()
            return 10

    def inverterPosicao(self):
        if(self.allPositions == [40,193,295]):
            self.allPositions == [91,244,142]
        else:
            self.allPositions == [40,193,295]
#encerrado por hoje
    def resetarPosicaoCarro(self):
        self.rect.x = self.allPositions[random.randint(0,2)]
        self.rect.y = 0 - 1 - self.rect.h