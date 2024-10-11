# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# switch axis to follow BlockManager logic
if self.ndim == 2:
    axis = 1 if axis == 0 else 0
exit(axis)
