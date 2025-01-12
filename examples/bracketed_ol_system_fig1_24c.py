"""
Example taken from the book:
    Przemyslaw Prusinkiewicz, Aristid Lindenmayer –
    [The Algorithmic Beauty of Plants PDF version available here for free Archived 2021-04-10 at the Wayback Machine]
    (https://en.wikipedia.org/wiki/The_Algorithmic_Beauty_of_Plants)

Section 1.6.3 Bracketed OL-systems
"""

from l_system.base import Lsystem
from l_system.rendering.renderer import LSystemRenderer
from l_system.rendering.turtle import TurtleConfiguration


class BracketedOlSystemFig124c(Lsystem):
    """Figure 1.24: Examples of plant-like structures generated by bracketed OL-systems. (c) Edge-rewriting system."""

    axiom = 'F'
    productions = {
        'F': 'FF-[-F+F+F]+[+F-F-F]',
    }
    recursions = 4


if __name__ == '__main__':
    lsystem = BracketedOlSystemFig124c()
    turtle_conf = TurtleConfiguration(angle=22.5, initial_heading_angle=90)
    renderer = LSystemRenderer(lsystem, turtle_conf, title="Bracketed OL-systems Fig 1.24c")
    renderer.draw()
