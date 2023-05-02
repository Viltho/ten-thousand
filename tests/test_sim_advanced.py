import pytest
from tests.flo import diff
from ten_thousand.game import play


def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest
    """
    diffs = diff(play, path="tests/repeat_roller.sim.txt")
    assert not diffs, diffs


def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    diffs = diff(play, path="tests/hot_dice.sim.txt")
    assert not diffs, diffs


def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user's input must be validated
    If invalid prompt user for re-entry
    """

    diffs = diff(play, path="tests/cheat_and_fix.sim.txt")
    assert not diffs, diffs


def test_zilcher():
    """
    No scoring dice results in a 'zilch'
    which wipes away shelved points
    and ends turn
    """

    diffs = diff(play, path="tests/zilcher.sim.txt")
    assert not diffs, diffs
