import pygame
from pygame.locals import *
import sys
import random
import time


speed = 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./image/png-transparent-car-transport-vehicle-yellow-automobile-top-view.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)

    def move(self):
        self.rect.move_ip(0,speed)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30,370),0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./image/png-transparent-car-transport-vehicle-yellow-automobile-top-view.png")
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)


    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



pygame.init()
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()
screen.fill((255,255,255))
pygame.display.set_caption("Cars")

p1 = Player()
e1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED:
            speed += 1

    p1.update()
    e1.move()
    screen.fill((255, 255, 255))
    for entity in all_sprites:
        entity.draw(screen)

    if pygame.sprite.spritecollideany(p1, enemies):
        screen.fill((255,0,0))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    clock.tick(60)