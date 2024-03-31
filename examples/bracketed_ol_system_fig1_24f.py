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


class BracketedOlSystemFig124f(Lsystem):
    """Figure 1.24: Examples of plant-like structures generated by bracketed OL-systems. (f) Node-rewriting system."""

    axiom = 'X'
    productions = {'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF'}
    recursions = 5


if __name__ == '__main__':
    lsystem = BracketedOlSystemFig124f()
    turtle_conf = TurtleConfiguration(angle=22.5, initial_heading_angle=90, turtle_move_mapper={'X': 'F'})
    renderer = LSystemRenderer(lsystem, turtle_conf, title="Bracketed OL-systems Fig 1.24f")
    renderer.draw()