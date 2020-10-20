import pygame
import random

class Arvore(pygame.sprite.Sprite):
    
    def __init__(self, grupo,id):
        super().__init__(grupo)
        self.setarArvore()
        self.id = id
        if(self.id == 1):
            self.rect.center = [410,-5]
        else:
            self.rect.center = [450, -300]

    def movimentarArvore(self):
        self.rect.move_ip([0,1])
    
    def checarFundo(self):
        if(self.rect.y <= 600):
            self.movimentarArvore()
        else:
            self.resetarPosicaoArvore()
    
    def resetarPosicaoArvore(self):
        self.setarArvore()
        if(self.id == 1):
            self.rect.center = [410, 0 - 1 - self.rect.h]
        else:
            self.rect.center = [450, 0 - 1 - self.rect.h]
    
    def getIntRandom(self):
        return random.randint(0,4)

    def getImgArvores(self):
        imgArvores = ["tree_1.png", "tree_2.png", "tree_3.png", "tree_4.png", "tree_5.png"]
        return imgArvores[self.getIntRandom()]
    
    def setarArvore(self):
        self.image = pygame.image.load(self.getImgArvores())
        self.rect = self.image.get_rect()