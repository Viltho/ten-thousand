import pytest
from tests.flo import diff
from ten_thousand.game import play



def test_game_complete():
    """Plays 1 round game and confirms proper exit
    IMPORTANT: pass 1 for num_rounds
    """
    diffs = diff(
        lambda roller: play(roller=roller, num_rounds=1), path="tests/complete.sim.txt"
    )
    assert not diffs, diffs
