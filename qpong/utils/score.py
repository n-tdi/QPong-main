"""
Game score
"""
import pygame


class Score(pygame.sprite.Sprite):
    """
    Score container for ongoing game
    """

    def __init__(self):
        super().__init__()

        self.player = 0
        self.computer = 0

    # Computer = 0, Player = 1
    def update(self, player):
        """
        Get score for a specified player

        Parameters:
        player (integer):
        """
        if player == 0:
            self.computer += 1

        if player == 1:
            self.player += 1

    def get_score(self, player):
        """
        Get score for a specified player

        Parameters:
        player (integer):
        """
        if player == 0:
            return self.computer
        return self.player

    def reset_score(self):
        """
        Reset score
        """
        self.computer = 0
        self.player = 0
