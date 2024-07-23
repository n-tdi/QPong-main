"""
Vertical pygame.sprite container
"""

import pygame

# pylint: disable=too-few-public-methods
class VBox(pygame.sprite.RenderPlain):
    """
    A container that arranges sprites vertically
    """

    def __init__(self, xpos, ypos, *sprites):
        pygame.sprite.RenderPlain.__init__(self, sprites)
        self.xpos = xpos
        self.ypos = ypos
        self.arrange()

    def arrange(self):
        """
        Arrange sprites vertically, each sucessive one going just
        above the previous
        """
        next_xpos = self.xpos
        next_ypos = self.ypos
        sprite_list = self.sprites()

        for sprite in sprite_list:
            sprite.rect.left = next_xpos
            sprite.rect.top = next_ypos
            next_ypos += sprite.rect.height
