#!/usr/bin/env python3
"""python_boilerplate."""
# %%
import python_boilerplate


# %%
def test_main_a_true() -> None:
    """A test_ok_sample."""
    assert 4 == python_boilerplate.main(1, 2)


# %%
def test_main_a_false() -> None:
    """A test_ok_sample."""
    assert 2 == python_boilerplate.main(2, 1)
