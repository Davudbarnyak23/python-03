import pygame, random, time , sys

IMAGES_PATH = 'images/imagesm/'
IMAGES_PATH1 = 'images/'
SCREEN_WIDTH = 18 * 40
SCREEN_HEIGHT = 18 * 30
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Bullet:
    bullet = None
    def __init__(self, x: int, y: int):
        self.bullet = pygame.Surface((3, 5))
        self.bullet.fill((0, 0, 50))

        self.x = x
        self.y = y
        self.speed = 2

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.bullet, (self.x, self.y))

class Bullets:
    bullet_list: list = []

    def add(self, x: int, y: int):
        b = Bullet(x, y)
        self.bullet_list.append(b)

    def move(self):
        for b in self.bullet_list:
            b.move()

            if b.y < 0:
                self.bullet_list.remove(b)

            b.draw()


class Player:
    moving: int = ''
    dt = 1
    bullets = None

    def __init__(self):
        self.image = pygame.image.load(IMAGES_PATH + 'player-walk-000.png')
        self.x = (SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - (self.image.get_height() + 10)
        self.speed = 5

        self.bullets = Bullets()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.moving == pygame.K_LEFT:
            self.move_left()
        if self.moving == pygame.K_RIGHT:
            self.move_right()


    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.image.get_width():
            self.x += self.speed
        else:
            self.x = SCREEN_WIDTH - self.image.get_width()

    def shoot(self):
        pass


class Bg:
    bg_image = None
    bg_surface = None

    def __init__(self):
        self.x = 0
        self.y = -SCREEN_HEIGHT
        self.speed = 1
        self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2))

        self.add_background()

    def add_background(self):
        self.bg_image = pygame.image.load(IMAGES_PATH + 'tile_0000.png')
        nx = int(SCREEN_WIDTH / self.bg_image.get_width()) + 1
        ny = int(SCREEN_HEIGHT / self.bg_image.get_height()) + 1
        w = self.bg_image.get_width()
        h = self.bg_image.get_height()

        for y in range(ny * 2):
            for x in range(nx):
                self.bg_surface.blit(self.bg_image, (w * x, h * y))

    def draw_background(self):
        self.y ++ self.speed

        if self.y >= 0:
            self.y = -SCREEN_HEIGHT

        screen.blit(self.bg_surface, (self.x, self.y))


class Game:
    bg_game = None
    game_run: bool = False

    def __init__(self):
        self.player = Player()
        self.bg_game = Bg()
        self.dt = 1
        self.interval = time.time()

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

        self.player.dt = self.dt

    def menu(self):
        im = pygame.image.load(IMAGES_PATH1 + 'bg_menu_1.jpg')
        screen.blit(im, (0, 0))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('key S', True, 'blue')
        screen.blit(text, (300, 100))

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event .type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

            self.menu()
            pygame.display.update()

    def run(self):
        self.game_run = True
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moving = pygame.K_LEFT
                    if event.key == pygame.K_RIGHT:
                        self.player.moving = pygame.K_RIGHT
                    if event.key == pygame.K_q:
                        self.game_run = False
                        break
                elif event.type == pygame.KEYUP:
                    self.player.moving = 0

            if self.game_run:
                self.bg_game.draw_background()
                self.player.move()
                self.player.draw()

                pygame.display.update()
        # end while


if __name__ == '__main__':
    game = Game()
    game.init()