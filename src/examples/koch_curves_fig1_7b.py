"""
Example taken from the book:
    Przemyslaw Prusinkiewicz, Aristid Lindenmayer –
    [The Algorithmic Beauty of Plants PDF version available here for free Archived 2021-04-10 at the Wayback Machine]
    (https://en.wikipedia.org/wiki/The_Algorithmic_Beauty_of_Plants)

Section 1.3
"""

from l_system.base import Lsystem
from l_system.rendering.turtle import TurtleConfiguration


class QuadraticSnowFlakeCurve(Lsystem):
    """Figure 1.7b Examples of Koch curves generated using L-systems: (b) A quadratic modification of the snowflake
    curve [95]"""

    axiom = '-F'
    productions = {'F': 'F+F-F-F+F'}
    recursions = 4


DEFAULT_TURTLE_CONFIG = TurtleConfiguration(angle=90, initial_heading_angle=90)
