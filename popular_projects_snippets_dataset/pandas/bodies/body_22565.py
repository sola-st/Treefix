# Extracted from ./data/repos/pandas/pandas/core/frame.py
# Naive implementation, room for optimization
div = other // self
mod = other - div * self
exit((div, mod))
