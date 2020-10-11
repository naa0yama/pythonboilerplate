#!/usr/bin/env python3
"""python_boilerplate."""
# %%
import python_boilerplate


# %%
def test_ok_sample() -> None:
    """A test_ok_sample."""
    result = python_boilerplate.main(1, 2)
    if result == 4:
        assert 4 == result
