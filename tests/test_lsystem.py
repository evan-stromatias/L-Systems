"""Testing the L-system implementation."""

import pytest

from tests.constants import Algae, FractalTree, KochCurve


@pytest.mark.parametrize("lsystem_cls", [Algae, FractalTree, KochCurve])
def test_lsystem(lsystem_cls):
    """Testing the functionality of L-system."""
    expected_results = lsystem_cls.expected()
    lsystem = lsystem_cls()
    for n, expected in expected_results:
        result = lsystem.apply(n)
        assert result == expected, (
            f"FAILED: '{lsystem_cls.name()}' L-system at iteration: {n}. ",
            f"Expected: '{expected}' != Actual: '{result}'",
        )
