import pygame
from pygame.locals import *
import os

pygame.init()

pygame.mixer.init()


screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Music Player")


font = pygame.font.Font(None, 36)


music_folder = "music"
music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]


current_music_index = 0


pygame.mixer.music.load(music_files[current_music_index])


pygame.mixer.music.play()


paused = False


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == K_LEFT:
                current_music_index -= 1
                if current_music_index < 0:
                    current_music_index = len(music_files) - 1
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()
                paused = False
            elif event.key == K_RIGHT:
                current_music_index += 1
                if current_music_index >= len(music_files):
                    current_music_index = 0
                pygame.mixer.music.load(music_files[current_music_index])
                pygame.mixer.music.play()
                paused = False

    screen.fill((255, 255, 255))
    text = font.render(os.path.basename(music_files[current_music_index]), True, (0, 0, 0))
    screen.blit(text, (50, 30))

    # Update the screen
    pygame.display.update()