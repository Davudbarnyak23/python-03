# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

screen_width = 800
screen_height = 600
# ініціалізація pygame
pygame.init()
# сворили вікно
screen = pygame.display.set_mode((screen_width, screen_height))
# интервом миж кадрами
clock = pygame.time.Clock()
clock_tick = 60

# заголовок вікна
pygame.display.set_caption('GTA_SPYDER')
#завантажуемо зображеня
spyder_image = pygame.image.load('images/spyder.png')
spyder_position = {'x':10, 'y':100}
#background = pygame.Surface((screen_width, screen_height))
#background.fill('purple')

background = pygame.image.load('images/background.jpg')

#text
count_fly = pygame.font.Font('font/Rock3D-Regular.ttf', 50)
text_count_fly = count_fly.render('Count: 0', False, 'blue')
#=============================================================
while True:
    #перевіряемо подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if spyder_position['y'] > 0:
            spyder_position['y'] -= 3
    if keys[pygame.K_s]:
        if spyder_position['y'] < screen_height - 110:
            spyder_position['y'] += 3
    if keys[pygame.K_a]:
        if spyder_position['x'] > 0:
            spyder_position['x'] -= 3
    if keys[pygame.K_d]:
        if spyder_position['x'] < screen_height - -100:
            spyder_position['x'] += 3


    #додаемо обект на екран
    screen.blit(background,(0, 0))
    screen.blit(spyder_image,(spyder_position['x'] , spyder_position['y']))
    screen.blit(text_count_fly, (500, 10))
    #оновлюваня екрану
    pygame.display.update()
    clock.tick(clock_tick)

