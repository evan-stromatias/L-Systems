"""
Example taken from the book:
    Przemyslaw Prusinkiewicz, Aristid Lindenmayer –
    [The Algorithmic Beauty of Plants PDF version available here for free Archived 2021-04-10 at the Wayback Machine]
    (https://en.wikipedia.org/wiki/The_Algorithmic_Beauty_of_Plants)

Section 1.3
"""

from l_system.base import Lsystem
from l_system.rendering.turtle import TurtleConfiguration


class KochCurvesFig19b(Lsystem):
    """Figure 1.9b"""

    axiom = 'F-F-F-F'
    productions = {
        'F': 'FF-F-F-F-FF',
    }
    recursions = 4


DEFAULT_TURTLE_CONFIG = TurtleConfiguration(initial_heading_angle=90)
