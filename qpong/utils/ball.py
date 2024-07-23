"""
A QPong ball
"""

import math
import random

import pygame

from qpong.utils.colors import WHITE
from qpong.utils.parameters import (
    WIDTH_UNIT,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    LEFT,
    RIGHT,
    NOTHING,
    NO,
    YES,
    MEASURE_LEFT,
    MEASURE_RIGHT,
)
from qpong.utils.score import Score
from qpong.utils.sound import Sound
from qpong.utils.resources import load_image


class Ball(pygame.sprite.Sprite):
    """
    A QPong ball
    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        super().__init__()

        # get ball screen dimensions
        self.screenheight = round(WINDOW_HEIGHT * 0.7)
        self.screenwidth = WINDOW_WIDTH
        self.width_unit = WIDTH_UNIT

        self.left_edge = self.width_unit
        self.right_edge = self.screenwidth - self.left_edge

        self.top_edge = self.width_unit * 0
        self.bottom_edge = self.screenheight - self.top_edge

        # define the ball sizes
        # self.height = self.width_unit
        # self.width = self.width_unit
        self.height = 32
        self.width = 32

        # create a pygame Surface with ball size
        # self.image = pygame.Surface([self.height, self.width])
        self.image, self.rect = load_image("player_images/Tilas-Kabengele.png", -1)

        # self.image.fill(WHITE)

        # self.rect = self.image.get_rect()

        self.xpos = 0
        self.ypos = 0
        self.speed = 0
        self.initial_speed_factor = 0.8
        self.direction = 0

        # initialize ball action type, measure and bounce flags
        self.ball_action = NOTHING
        self.measure_flag = NO

        # initialize ball reset on the left
        self.reset_position = LEFT
        self.reset()

        self.sound = Sound()
        self.score = Score()

    def update(self):
        """
        Update ball
        """
        radians = math.radians(self.direction)

        self.xpos += self.speed * math.sin(radians)
        self.ypos -= self.speed * math.cos(radians)

        # Update ball position
        self.rect.x = self.xpos
        self.rect.y = self.ypos

        if self.ypos <= self.top_edge:
            self.direction = (180 - self.direction) % 360
            self.sound.edge_sound.play()
        if self.ypos > self.bottom_edge - 1 * self.height:
            self.direction = (180 - self.direction) % 360
            self.sound.edge_sound.play()

    def reset(self):
        """
        Reset ball position and speed to initial settings.
        """
        self.ypos = self.screenheight / 2
        self.speed = self.width_unit * self.initial_speed_factor

        # alternate reset at left and right
        if self.reset_position == LEFT:
            self.xpos = self.left_edge + self.width_unit * 15
            self.direction = random.randrange(30, 120)
            self.reset_position = RIGHT
        else:
            self.xpos = self.right_edge - self.width_unit * 15
            self.direction = random.randrange(-120, -30)
            self.reset_position = LEFT

    def bounce_edge(self):
        """
        Bounce ball off a screen edge
        """
        self.direction = (360 - self.direction) % 360
        self.speed *= 1.1
        self.sound.bounce_sound.play()

    def get_xpos(self):
        """
        Get ball's x position
        """
        xpos = self.xpos
        return xpos

    def get_ypos(self):
        """
        Get ball's y position
        """
        ypos = self.ypos
        return ypos

    # 1 = comp, 2 = player, none = 0
    def action(self):
        """
        Decide ball action based on the ball's position
        """
        if self.xpos < self.left_edge:
            # reset the ball when it reaches beyond left edge
            self.reset()
            self.sound.lost_sound.play(3)
            self.score.update(1)

        elif (
            self.left_edge + 10 * self.width_unit
            <= self.xpos
            < self.left_edge + 12 * self.width_unit
        ):
            # measure the ball when it reaches the left measurement zone
            if self.measure_flag == NO:
                self.ball_action = MEASURE_LEFT
                self.measure_flag = YES
            else:
                self.ball_action = NOTHING

        elif (
            self.right_edge - 12 * self.width_unit
            <= self.xpos
            < self.right_edge - 10 * self.width_unit
        ):
            # measure the ball when it reaches the right measurement zone
            if self.measure_flag == NO:
                # do measurement if not yet done
                self.ball_action = MEASURE_RIGHT
                self.measure_flag = YES
            else:
                # do nothing if measurement was done already
                self.ball_action = NOTHING

        elif self.xpos > self.right_edge:
            # reset the ball when it reaches beyond right edge
            self.reset()
            self.sound.lost_sound.play(3)
            self.score.update(0)

        else:
            # reset flags and do nothing when the ball is outside measurement and bounce zone
            self.ball_action = NOTHING
            self.measure_flag = NO

    def check_score(self, player):
        """
        Check a player score
        """
        return self.score.get_score(player)
