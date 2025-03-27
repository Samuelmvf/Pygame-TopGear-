import pygame
from src.player import Player
from src.tree import Tree
from src.enemy import Enemy
import time
#initializing pygame
pygame.init()

#CONSTANTS
W_SIZE = W_WIDTH, W_HEIGHT = 500, 600
LANES = [[40, 140], [144, 244], [248, 348]]
 #Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_DARK = (232, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
GREY_DARK = (94, 94, 94)
#font
font_score = pygame.font.Font('freesansbold.ttf', 65)
font_gameOver = pygame.font.SysFont(None, 55)
# defining the text


#Defining Sprites
    #DRAWGROUP
drawGroup = pygame.sprite.Group()
    #SPRITES
player = Player(drawGroup)
tree1 = Tree(drawGroup, 0)
tree2 = Tree(drawGroup, 1)
enemy1 = Enemy(drawGroup, 0)
enemy2 = Enemy(drawGroup, 1)

#defining display size, window name and icon
pygame.display.set_mode(W_SIZE)
display = pygame.display.get_surface()
pygame.display.set_caption('Car Racing')
pygame.display.set_icon(pygame.image.load('assets/gameicon.png'))

#condition for game to continue
gameLoop = True
#Defining Clock
clock = pygame.time.Clock()
#Defining difficulty
BASE_SPEED = 100
NEXT_LEVEL_INCREMENT = 20
#Music
pygame.mixer.music.load('assets/top-Gear-Soundtrack.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#functions

def drawScreen():
    #Drawing screen
    display.fill(WHITE)
    pygame.draw.rect(display, GREEN, (0, 0, W_WIDTH, W_HEIGHT))
    pygame.draw.rect(display, WHITE, (LANES[0][0], 0, LANES[2][1] - LANES[0][0], W_HEIGHT))
    pygame.draw.rect(display, GREY, (LANES[0][0], 0, LANES[0][1] - LANES[0][0], W_HEIGHT))
    pygame.draw.rect(display, GREY, (LANES[1][0], 0, LANES[1][1] - LANES[1][0], W_HEIGHT))
    pygame.draw.rect(display, GREY, (LANES[2][0], 0, LANES[2][1] - LANES[2][0], W_HEIGHT))
    #Drawing Cars
    drawGroup.draw(display)
    pygame.display.update()

def checkCollision():
    collision = False
    if((player.rect.top <= enemy1.rect.bottom and player.rect.top >= enemy1.rect.top) or (player.rect.bottom <= enemy1.rect.bottom and player.rect.bottom >= enemy1.rect.top)):
        if(player.rect.right >= enemy1.rect.left and player.rect.right <= enemy1.rect.right):
            collision = True
        if(player.rect.left >= enemy1.rect.left and player.rect.left <= enemy1.rect.right):
            collision = True

    if((player.rect.top <= enemy2.rect.bottom and player.rect.top >= enemy2.rect.top) or (player.rect.bottom <= enemy2.rect.bottom and player.rect.bottom >= enemy2.rect.top)):
        if(player.rect.right >= enemy2.rect.left and player.rect.right <= enemy2.rect.right):
            collision = True
        if(player.rect.left >= enemy2.rect.left and player.rect.left <= enemy2.rect.right):
            collision = True

    if(collision):
        player.car_after_accident()
        drawScreen()
    return collision

index = 1
score = 0
multiplier = 1
while gameLoop:
    if score != 0:
        if score % 50 == 0:
            multiplier = 1 + (score / 50)

    clock.tick(BASE_SPEED + (NEXT_LEVEL_INCREMENT * multiplier))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
            pygame.mixer.music.stop()
    keys = pygame.key.get_pressed()
    
    if(checkCollision()):
        text_gameOver = font_gameOver.render('GAME OVER!', True, RED_DARK)
        display.blit(text_gameOver, [120,60])

        font_custom1 = pygame.font.Font('freesansbold.ttf', 45)
        text1 = font_custom1.render("Your score was: " + str(score), True, BLACK)
        display.blit(text1, [40,120])

        font_custom2 = pygame.font.Font('freesansbold.ttf', 44)
        text2 = font_custom2.render("Your score was: " + str(score), True, WHITE)
        display.blit(text2, [47,120])

        font_custom3 = pygame.font.Font('freesansbold.ttf', 25)
        font_custom4 = pygame.font.Font('freesansbold.ttf', 24)

        text3 = font_custom3.render("Press R to exit", True, BLACK)
        display.blit(text3, [100,180])

        pygame.display.flip()

        controller = True
        while controller:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        controller = False
                        gameLoop = False
                        pygame.quit()
    else:
        tree1.check_bottom()
        tree2.check_bottom()
        if(index % 2 == 0):
            enemy1.invert_position()
            enemy2.invert_position()
        score += enemy1.check_bottom()
        score += enemy2.check_bottom()
        
        if keys[pygame.K_UP]:
            player.move_up()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_DOWN]:
            player.move_down()

        drawScreen()
        text_score = font_score.render(str(score), True, BLACK)
        display.blit(text_score, [W_WIDTH - 200, 10])
        pygame.display.flip()
    
    index = index + 1