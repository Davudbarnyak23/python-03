import pygame

pygame.init()
display = pygame.display.set_mode((100, 100), pygame.RESIZABLE)
pygame.display.set_caption('mouse')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            print('x={}, y={}'.format(pos[0], pos[1]))
            print(btn)
