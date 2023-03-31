import pygame
import sys

red = (255,0,0)
black = (0,0,0)

border = 20
window_width =640
window_height = 480
speed = 20

player_x = window_width / 2
player_y = window_height /2

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

pygame.init()

pygame.draw.rect(screen, black, (0,0, window_width, border))
pygame.draw.rect(screen, black, (0,0, border, window_height))
pygame.draw.rect(screen, black, (0,window_height - border, window_width, border))
pygame.draw.rect(screen, black, (window_width - border, 0, border, window_height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,0,0))

    pygame.draw.rect(screen, black, (0, 0, window_width, border))
    pygame.draw.rect(screen, black, (0, 0, border, window_height))
    pygame.draw.rect(screen, black, (0, window_height - border, window_width, border))
    pygame.draw.rect(screen, black, (window_width - border, 0, border, window_height))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_y > border:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < window_height - border:
        player_y += speed
    if keys[pygame.K_RIGHT] and player_x < window_width - border:
        player_x += speed
    if keys[pygame.K_LEFT] and player_x > border:
        player_x -= speed

    pygame.draw.circle(screen, red, (player_x, player_y), 25)

    clock.tick(60)
    pygame.display.flip()



