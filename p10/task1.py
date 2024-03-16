# Розкоментувати і виправити помилки в програмі

import sys
import pygame

pygame.init()
run = True
window = pygame.display.set_mode((600, 600))
SkyColor = (124, 255, 235)
window.fill(SkyColor)
hero = pygame.image.load("images/pikachu.png")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(hero, (44, 64))
    pygame.display.flip()