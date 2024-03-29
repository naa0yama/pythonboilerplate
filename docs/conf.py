#!/usr/bin/env python3
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""conf."""
# Standard Library
import os
import sys

# Third Party Library
from sphinx_pyproject import SphinxConfig

sys.path.append(
    os.path.abspath(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__),
            ),
        ),
    ),
)

config = SphinxConfig(
    os.path.join(
        os.path.abspath(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)),
            ),
        ),
        "pyproject.toml",
    ),
    globalns=globals(),
)
