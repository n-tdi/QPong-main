"""
Various fonts used through out the game
"""

from qpong.utils.parameters import WIDTH_UNIT

from qpong.utils.resources import load_font

# pylint: disable=too-few-public-methods
class Font:
    """
    Load fonts
    """

    def __init__(self):
        self.gameover_font = load_font("bit5x3.ttf", 10 * WIDTH_UNIT)
        self.credit_font = load_font("bit5x3.ttf", 2 * WIDTH_UNIT)
        self.replay_font = load_font("bit5x3.ttf", 5 * WIDTH_UNIT)
        self.score_font = load_font("bit5x3.ttf", 12 * WIDTH_UNIT)
        self.vector_font = load_font("bit5x3.ttf", 3 * WIDTH_UNIT)
        self.player_font = load_font("bit5x3.ttf", 3 * WIDTH_UNIT)
