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


class IslandsAndLakes(Lsystem):
    """Figure 1.8: Combination of islands and lakes [95,page121]"""

    axiom = 'F+F+F+F'
    productions = {'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF', 'f': 'ffffff'}
    recursions = 2


if __name__ == '__main__':
    lsystem = IslandsAndLakes()
    turtle_conf = TurtleConfiguration(forward_step=3)
    renderer = LSystemRenderer(l_system=lsystem, turtle_configuration=turtle_conf, title="Islands and Lakes")
    renderer.draw()
