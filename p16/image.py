import pygame

IMG_LOCATION = 'Sprites/location/'
IMG_SHIP = 'Sorites/ship/s1/Ship/'
pygame.init()
screen = pygame.display.set_mode((600, 600))

img2 = pygame.image.load(IMG_LOCATION + 'bg-02.jpeg')
img1 = pygame.image.load(IMG_SHIP + 'Ship1.png')
deg = 0;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.K_r:
            deg += 1
            img1 = pygame.transform.rotate(img1, deg)

    screen.fill((127, 127, 127))
    screen.blit(img2, (20, 100))
    screen.blit(img1, (120, 200))
    pygame.display.update()