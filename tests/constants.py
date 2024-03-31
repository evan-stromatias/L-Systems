from l_system.base import Lsystem


class Algae(Lsystem):
    """Lindenmayer's original L-system for modelling the growth of algae."""

    axiom = 'A'
    productions = {'A': 'AB', 'B': 'A'}

    @classmethod
    def expected(cls) -> list[tuple[int, str]]:
        return [(0, "A"), (1, "AB"), (2, "ABA"), (3, "ABAAB"), (7, "ABAABABAABAABABAABABAABAABABAABAAB")]


class FractalTree(Lsystem):
    """A fractal (binary) tree L-system"""

    axiom = '0'
    productions = {'1': '11', '0': '1[0]0'}

    @classmethod
    def expected(cls) -> list[tuple[int, str]]:
        return [
            (0, "0"),
            (1, "1[0]0"),
            (2, "11[1[0]0]1[0]0"),
            (3, "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0"),
        ]


class KochCurve(Lsystem):
    """A variant of the Koch curve which uses only right angles."""

    axiom = 'F'
    productions = {
        'F': 'F+F-F-F+F',
    }

    @classmethod
    def expected(cls) -> list[tuple[int, str]]:
        return [
            (0, "F"),
            (1, "F+F-F-F+F"),
            (2, "F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F"),
            (
                3,
                (
                    "F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F"
                    "-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+F+F-F-F+F+"
                    "F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F"
                ),
            ),
        ]
