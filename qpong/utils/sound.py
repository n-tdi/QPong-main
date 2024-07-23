"""
Utility class for loading game sounds
"""

from qpong.utils.resources import load_sound

# pylint: disable=too-few-public-methods
class Sound:
    """
    Load sounds
    """

    def __init__(self):
        self.bounce_sound = load_sound("4391__noisecollector__pongblipf-5.wav")
        self.edge_sound = load_sound("4390__noisecollector__pongblipf-4.wav")
        self.lost_sound = load_sound("4384__noisecollector__pongblipd4.wav")
