#нужны улучшение 


import pygame
import sys
import subprocess

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Выбор игры')

font = pygame.font.Font(None, 74)
clock = pygame.time.Clock()

running = True

def draw_menu():
    screen.fill((0, 0, 0))
    text = font.render('Нажми 3 или 5', True, (255, 255, 255))
    screen.blit(text, (150, 150))
    pygame.display.flip()

while running:
    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                subprocess.run([sys.executable, "c:\\Users\\Huawei\\Desktop\\gdg\\xo\\xo3.py"])
            elif event.key == pygame.K_5:
                subprocess.run([sys.executable, "c:\\Users\\Huawei\\Desktop\\gdg\\xo\\xo5.py"])

    clock.tick(60)

pygame.quit()
sys.exit()
