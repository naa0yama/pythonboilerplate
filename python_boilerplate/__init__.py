#!/usr/bin/env python3
"""python_boilerplate."""


# %%
def main(a: int, b: int) -> int:
    """main."""
    if a == 1:
        b = b + 1
    else:
        b = b - 1
    return a + b
