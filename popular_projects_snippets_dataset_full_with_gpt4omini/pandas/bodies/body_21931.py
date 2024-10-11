# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
on = self.on
if on is None:
    if self.axis == 0:
        on = "index"
    else:
        on = "column"
raise ValueError(f"{on} {msg}")
