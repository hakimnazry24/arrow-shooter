import pygame
from settings import *
from pygame.locals import *
import sys
from sprites.player import Player
from surfaces.background import Background


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Arrow Shooter")
        self.DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.frame_per_sec = pygame.time.Clock()
        self.background = Background()

    def load_sprites(self):
        player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(player)

    def on_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def on_update(self):
        for sprite in self.all_sprites:
            sprite.draw(self.DISPLAYSURF)
            sprite.move()

    def on_execute(self):
        self.load_sprites()

        while True:
            self.DISPLAYSURF.blit(self.background.bg_surface, (0, 0))
            self.on_events()
            self.on_update()

            pygame.display.update()
            self.frame_per_sec.tick(FPS)


if __name__ == "__main__":
    app = App()
    app.on_execute()
