"""
QPong game
"""

import os

from .containers import *
from .utils import *
from .viz import *
from .model import *
from .controls import *

with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "VERSION.txt")), "r"
) as _ver_file:
    __version__ = _ver_file.read().rstrip()
