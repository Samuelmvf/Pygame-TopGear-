import pygame
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, id):
        super().__init__(group)
        self.id = id
        self.image = (pygame.image.load('assets/cars/blue_car.png') if id == 0 else pygame.image.load('assets/cars/red_car.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (250, -20)
        self.all_positions = [40,193,295] if id == 0 else [91,244,142]
        self.rect.x = self.all_positions[self.id]
    
    def move_car(self):
        if(self.id == 0):
            self.rect.move_ip([0,1])
        else:
            self.rect.move_ip([0,2])            
    
    def get_random_position(self):
        return random.randint(40,298)
    
    def check_bottom(self):
        if(self.rect.y <= 600):
            self.move_car()
            return 0
        else:
            self.reset_car_position()
            return 10

    def invert_position(self):
        if(self.all_positions == [40,193,295]):
            self.all_positions == [91,244,142]
        else:
            self.all_positions == [40,193,295]
#finished for today
    def reset_car_position(self):
        self.rect.x = self.all_positions[random.randint(0,2)]
        self.rect.y = 0 - 1 - self.rect.h