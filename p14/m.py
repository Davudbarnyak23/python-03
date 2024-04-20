import pygame

screen_width: int = 600
screen_height: int = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Game:
    run: bool = True

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

        # END WHILE -------------------------------------

        pygame.quit()


g = Game()
g.play()