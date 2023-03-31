import pygame
import datetime
import sys, os
import math



pygame.init()
width, height = 800,600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption("Clock")
screen.fill((0,0,0))

current_time = datetime.datetime.now()
seconds = current_time.second
minutes = current_time.minute


clock_image = pygame.transform.scale(pygame.image.load('./image/mickeyclock.jpeg'), (800, 600))
min_arrow = pygame.image.load(r'./image/minhand.png')
min_arrow = pygame.transform.scale(min_arrow, (250,75))
minhand = min_arrow.get_rect()
minhand.center = (400,300)

sec_arrow = pygame.image.load(r'./image/sechand.png')
sec_arrow = pygame.transform.scale(sec_arrow, (250,75))
sechand = sec_arrow.get_rect()
sechand.center = (400,300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    screen.fill(0)
    screen.blit(clock_image, (0, 0))

    minute_rotation = pygame.transform.rotate(min_arrow, -1 * (6 * minutes) - 160)
    minute_rotation_obj = minute_rotation.get_rect()
    minute_rotation_obj.center = minhand.center
    pygame.display.update()
    screen.blit(minute_rotation, minute_rotation_obj)

    second_rotation = pygame.transform.rotate(sec_arrow, -1 * (6 * seconds)  + 90)
    second_rotation_obj  = second_rotation.get_rect()
    second_rotation_obj.center = sechand.center
    pygame.display.flip()
    screen.blit(second_rotation, second_rotation_obj)

    pygame.display.update()
    clock.tick(60)
    current_time = datetime.datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

