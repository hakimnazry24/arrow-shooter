import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    ASSETS_PATH = "./assets/character/Warrior_03__"

    def __init__(self):
        super().__init__()
        self.images_idle = [
            f"{Player.ASSETS_PATH}IDLE_000.png",
            f"{Player.ASSETS_PATH}IDLE_001.png",
            f"{Player.ASSETS_PATH}IDLE_002.png",
        ]
        self.images_walk = [
            f"{Player.ASSETS_PATH}WALK_000.png",
            f"{Player.ASSETS_PATH}WALK_001.png",
            f"{Player.ASSETS_PATH}WALK_002.png",
        ]
        self.image = pygame.image.load(self.images_idle[0])
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.right_facing_image = self.image
        self.left_facing_image = pygame.transform.flip(self.right_facing_image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.counter = 0
        self.facing_direction = "right"

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.facing_direction = "left"
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.facing_direction = "right"
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        if self.facing_direction == "left":
            surface.blit(self.left_facing_image, self.rect)
        elif self.facing_direction == "right":
            surface.blit(self.right_facing_image, self.rect)
            