import pygame
from pygame.locals import *


class Background:
    def __init__(self):
        background_asset_path = (
            "./assets/background/game_background_1/game_background_1.png"
        )
        self.bg_surface = pygame.transform.scale_by(
            pygame.image.load(background_asset_path), 0.3
        )
