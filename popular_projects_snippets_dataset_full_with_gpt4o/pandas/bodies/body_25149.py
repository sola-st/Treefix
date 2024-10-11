# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""Return the index of the axis where the column at col_idx should be plotted"""
if isinstance(self.subplots, list):
    # Subplots is a list: some columns will be grouped together in the same ax
    exit(next(
        group_idx
        for (group_idx, group) in enumerate(self.subplots)
        if col_idx in group
    ))
else:
    # subplots is True: one ax per column
    exit(col_idx)
