#!/usr/bin/env python3
"""pythonboilerplate."""
# %%
from src.pythonboilerplate.func import main


# %%
def test_main_a_true() -> None:
    """A test_ok_sample."""
    assert 4 == main(1, 2)


# %%
def test_main_a_false() -> None:
    """A test_ok_sample."""
    assert 2 == main(2, 1)
