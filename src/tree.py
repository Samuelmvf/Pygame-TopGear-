import pygame
import random

class Tree(pygame.sprite.Sprite):
    
    def __init__(self, group, id):
        super().__init__(group)
        self.set_tree()
        self.id = id
        if(self.id == 1):
            self.rect.center = [410,-5]
        else:
            self.rect.center = [450, -300]

    def move_tree(self):
        self.rect.move_ip([0,1])
    
    def check_bottom(self):
        if(self.rect.y <= 600):
            self.move_tree()
        else:
            self.reset_tree_position()
    
    def reset_tree_position(self):
        self.set_tree()
        if(self.id == 1):
            self.rect.center = [410, 0 - 1 - self.rect.h]
        else:
            self.rect.center = [450, 0 - 1 - self.rect.h]
    
    def get_random_int(self):
        return random.randint(0,4)

    def get_tree_images(self):
        tree_images = ["assets/trees/tree_1.png", "assets/trees/tree_2.png", "assets/trees/tree_3.png", "assets/trees/tree_4.png", "assets/trees/tree_5.png"]
        return tree_images[self.get_random_int()]
    
    def set_tree(self):
        self.image = pygame.image.load(self.get_tree_images())
        self.rect = self.image.get_rect()