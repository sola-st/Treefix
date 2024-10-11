# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if len(start) != len(end):
    raise ValueError(
        f"start ({len(start)}) and end ({len(end)}) bounds must be the "
        f"same length"
    )
if len(start) != (num_vals + (self.step or 1) - 1) // (self.step or 1):
    raise ValueError(
        f"start and end bounds ({len(start)}) must be the same length "
        f"as the object ({num_vals}) divided by the step ({self.step}) "
        f"if given and rounded up"
    )
