import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Wilhelm_Scream.ogg")
display_width = 900
display_height = 750
car_width = 55

#showing the game box and title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fury Road')

sand = (150,113,23)
chrome = (140,146,172)

clock = pygame.time.Clock()
sprite = pygame.image.load('pipe_car.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(sprite, (x,y))

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    time.sleep(1.5)
    game_loop()

def game_loop():
    pygame.mixer.music.load('road_warrior.ogg')
    pygame.mixer.music.play(-1)
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
        
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 300
    thing_height = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        gameDisplay.fill(sand)
        x += x_change

        things(thing_startx, thing_starty, thing_width, thing_height, chrome)
        thing_starty += thing_speed
        car(x,y)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)

        if x > display_width - car_width or x < 0:
            crash()

        if y < thing_starty+thing_height:
          if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crash()
            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()