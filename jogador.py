import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('white_car.png')
        self.rect = self.image.get_rect()
        self.rect.center = (250, 499)
    
    def carroPosAcidente(self):
        self.image = pygame.image.load('white_car_2.png')

    def moverParaCima(self):
        if(self.rect.y >= 1):
            self.rect.y -= 1

    def moverParaBaixo(self):
        if(self.rect.y <= 499):
            self.rect.y += 1

    def moverParaDireita(self):
        if(self.rect.x < 298):
            self.rect.x += 1
            
    def moverParaEsquerda(self):
        if(self.rect.x > 40):
            self.rect.x -= 1