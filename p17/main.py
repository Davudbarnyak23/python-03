import pygame, random, time, sys, asyncio

IMAGES_PATH = 'images/imagesm/'
IMAGES_PATH1 = 'images/'
IMAGES_MENU_PATH = 'images/menu/'
IMAGES_BG_PATH = 'images/background/'
FONTS_PATH = 'fonts/'
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

        self.x = x + 9
        self.y = y
        self.speed = 5

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
    moving: list = []
    dt = 1
    bullets = None

    def __init__(self):
        self.image = pygame.image.load(IMAGES_PATH + 'player-walk-000.png')
        self.x = (SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - (self.image.get_height() + 10)
        self.speed = 3

        self.bullets = Bullets()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if len(self.moving) > 0:
            if self.moving[0] == pygame.K_LEFT:
                self.move_left()
            elif self.moving[0] == pygame.K_RIGHT:
                self.move_right()

        self.bullets.move()

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
        self.bullets.add(self.x, self.y)


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
        self.y += self.speed

        if self.y >= 0:
            self.y = -SCREEN_HEIGHT

        screen.blit(self.bg_surface, (self.x, self.y))


class Menu:
    def __init__(self):

        bg_img = pygame.image.load(IMAGES_MENU_PATH + 'bg-02.jpg')
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        box_img = pygame.image.load(IMAGES_MENU_PATH + 'Cloud_02.png')
        self.box_img = pygame.transform.scale(box_img, (300, 300))

    def start_btn(self):
        color = (0, 0, 0)

        if self.start_pos():
            color = (255, 250, 250)

        font = pygame.font.SysFont(FONTS_PATH + 'Jersey25Charted-Regular.ttf', 40)
        text = font.render('START key s', True, color)
        screen.blit(text, (270, 150))  # 440 170

    def draw(self):
        screen.blit(self.bg_img, (0, 0))
        screen.blit(self.box_img, (210, 110))
        self.start_btn()


    def start_pos(self):
        pos = pygame.mouse.get_pos()


        if (pos[0] > 270 and pos[0] < 440 and pos[1] > 150 and pos[1] < 170):
            return True

        return False

    def mouse_click(self):
        b = pygame.mouse.get_pressed()

        if self.start_pos() and b[0]:
            return 'run'

        return None


# class Enemy:
#     x: int = 0
#     y: int = 0
#     speed: int = 0
#     image = None
#
#     def add(self):
#         pass
#
#     def move(self):
#         pass
#
#     def fire(self):
#         pass


enemies_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(IMAGES_PATH + 'tile_0009.png')
        x, y = random.randint(50, SCREEN_WIDTH-50), random.randint(-100, -50)
        self.rect = self.image.get_rect(center=(x, y))

        self.speen = random.randint(3, 7)


    def update(self, dt):
        self.rect.centery += 2 #self.speed * dt

        if self.rect.centery > SCREEN_HEIGHT - 100:
            self.kill()


class Game:
    bg_game = None
    game_run: bool = False

    def __init__(self):
        self.player = Player()
        self.bg_game = Bg()
        self.dt = 1
        self.interval = time.time()
        self.menu = Menu()
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, random.randint(1000, 3000))

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

        self.player.dt = self.dt


    async def init(self):
        while True:
            if self.game_run:
                self.run()
            else:
                self.main_menu()

            pygame.display.update()
            await  asyncio.sleep(0)
    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.game_run = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu.mouse_click() == 'run':
                    self.game_run = True

        self.menu.draw()

    def run(self):
        self.delta_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if event.key not in self.player.moving:
                        self.player.moving.append(event.key)
                elif event.key == pygame.K_SPACE:
                    self.player.shoot()
                elif event.key == pygame.K_q:
                    self.game_run = False
                    break
            elif event.type == pygame.KEYUP:
                if event.key in self.player.moving:
                    self.player.moving.remove(event.key)
            if event.type == self.enemy_event:
                Enemy(enemies_group)

        if self.game_run:
            self.bg_game.draw_background()
            self.player.move()
            self.player.draw()
            enemies_group.update(self.dt)
            enemies_group.draw(screen)

if __name__ == '__main__':
    game = Game()
    asyncio.run(game.init())