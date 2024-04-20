import pygame
def draw_background(screen, picture):
    screen.blit(background, (0, 0))

def main():
    run = True

    pygame.init()
    screen_width: int = 600
    screen_height: int = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    background_picture(screen,'images/background.png')

     while run:
         draw_background(screen, background_picture)

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False