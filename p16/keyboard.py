import pygame

pygame.init()
display = pygame.display.set_mode((100, 100), pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print('doun ', key)
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print("up" , key)

