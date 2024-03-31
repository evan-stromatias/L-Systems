"""
Example taken from the book:
    Przemyslaw Prusinkiewicz, Aristid Lindenmayer –
    [The Algorithmic Beauty of Plants PDF version available here for free Archived 2021-04-10 at the Wayback Machine]
    (https://en.wikipedia.org/wiki/The_Algorithmic_Beauty_of_Plants)

Section 1.3
"""

from l_system.base import Lsystem
from l_system.rendering.renderer import LSystemRenderer
from l_system.rendering.turtle import TurtleConfiguration


class KochCurvesFig19f(Lsystem):
    """Figure 1.9f"""

    axiom = 'F-F-F-F'
    productions = {
        'F': 'F-F+F-F-F',
    }
    recursions = 4


if __name__ == '__main__':
    lsystem = KochCurvesFig19f()
    turtle_conf = TurtleConfiguration(initial_heading_angle=90)
    renderer = LSystemRenderer(lsystem, turtle_conf)
    renderer.draw()
