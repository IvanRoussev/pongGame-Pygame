from ast import Pass
from cgitb import text
import pygame
pygame.init()

pygame.display.set_caption("PONG")
WIDTH = 700
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmall = pygame.font.Font('freesansbold.ttf', 25)

GREEN = (0,255,0)





def draw(window):
    window.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(250, 320, 200, 50))
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(250, 400, 200, 50))

    text = font.render('Welcome To Pong', True, GREEN)
    WINDOW.blit(text, [200, 100])

    rankedText = fontSmall.render('Ranked', True, GREEN)
    WINDOW.blit(rankedText, [280, 420])

    FreeText = fontSmall.render('Free Play', True, GREEN)
    WINDOW.blit(FreeText, [280, 340])
    pygame.display.flip()

def screenClick(click):
    pass
   

def main():
    run = True
    clock = pygame.time.Clock()

  

    while run:
            
                
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pos[0] >= 250 and pos[0] <= 450) and (pos[1] >= 320 and pos[1] <= 370):
                    print('CLICKED FREE PLAY')
                
                elif (pos[0] >= 250 and pos[0] <= 450) and (pos[1] >= 400 and pos[1] <= 450):
                    print('CLICKED RANKED')

                elif event.type == pygame.QUIT:
                    run = False
                    break

        draw(WINDOW)
        clock.tick(FPS)

        
    pygame.quit()

if __name__ == '__main__':
    main()

