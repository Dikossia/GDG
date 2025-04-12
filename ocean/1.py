import pygame 
import random , sys

white = (255, 255, 255)
black = (0, 0, 0)

block = 30
left_margin = 40
top_margin = 50

size = (left_margin + 30*block, top_margin + 15*block)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleship")

font_size = int(block // 1.5)
font = pygame.font.SysFont("Arial", font_size)

def draw_grid():
    for y in range (11):
        for x in range(11):
             pygame.draw.line(screen, black, (left_margin, top_margin +y*block), (left_margin +10*block, top_margin + y*block), 1)
             pygame.draw.line(screen,black, (left_margin + x*block, top_margin), (left_margin + x*block, top_margin + 10*block), 1)
             pygame.draw.line(screen, black, (left_margin + 15*block, top_margin +y*block), (left_margin +25*block, top_margin + y*block), 1)
             pygame.draw.line(screen,black, (left_margin + x*block + 15*block, top_margin), (left_margin + x*block +15*block, top_margin + 10*block), 1)
def main():
    game_over = False
    screen.fill(white)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        draw_grid()
        pygame.display.update()

main()
pygame.quit()