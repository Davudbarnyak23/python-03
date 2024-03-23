import pygame
pygame.init()

screen = pygame.display.set_mode((600,400))
def draw_circle(action):
    if action == 'clear':
        color = (0, 0, 0)
    if action == 'paint':
        color = (15, 66, 88)
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, color, pos,18)
    pygame.display.update()


def main():
    mouse_button = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sy.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    draw_circle('paint')
                    mouse_button = True
                if event.button == 3:
                    draw_circle('clear')
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_button = False


            # if mouse_button:
            #     draw_circle(PAINT_CIRCLE)22



main()