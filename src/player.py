import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('assets/white_car.png')
        self.rect = self.image.get_rect()
        self.rect.center = (250, 499)
    
    def car_after_accident(self):
        self.image = pygame.image.load('assets/white_car_2.png')

    def move_up(self):
        if(self.rect.y >= 1):
            self.rect.y -= 1

    def move_down(self):
        if(self.rect.y <= 499):
            self.rect.y += 1

    def move_right(self):
        if(self.rect.x < 298):
            self.rect.x += 1
            
    def move_left(self):
        if(self.rect.x > 40):
            self.rect.x -= 1