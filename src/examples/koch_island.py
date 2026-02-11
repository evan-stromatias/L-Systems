"""
Example taken from the book:
    Przemyslaw Prusinkiewicz, Aristid Lindenmayer –
    [The Algorithmic Beauty of Plants PDF version available here for free Archived 2021-04-10 at the Wayback Machine]
    (https://en.wikipedia.org/wiki/The_Algorithmic_Beauty_of_Plants)

Section 1.3
"""

from l_system.base import Lsystem
from l_system.rendering.turtle import TurtleConfiguration


class KochIsland(Lsystem):
    """Figure 1.6: Generating a quadratic Koch island"""

    axiom = 'F-F-F-F'
    productions = {
        'F': 'F-F+F+FF-F-F+F',
    }
    recursions = 3


DEFAULT_TURTLE_CONFIG = TurtleConfiguration(forward_step=3, angle=90)
