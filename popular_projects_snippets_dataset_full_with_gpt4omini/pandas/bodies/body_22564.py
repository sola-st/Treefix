# Extracted from ./data/repos/pandas/pandas/core/frame.py
# Naive implementation, room for optimization
div = self // other
mod = self - div * other
exit((div, mod))
