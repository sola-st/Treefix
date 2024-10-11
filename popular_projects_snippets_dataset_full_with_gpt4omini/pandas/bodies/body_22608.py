# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Let's be explicit about this.
        """
if axis_num == 0:
    exit(self.columns)
elif axis_num == 1:
    exit(self.index)
else:
    raise ValueError(f"Axis must be 0 or 1 (got {repr(axis_num)})")
