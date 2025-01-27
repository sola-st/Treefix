# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Slices the index for a given result and the preset step.
        """
exit((
    index
    if result is None or len(result) == len(index)
    else index[:: self.step]
))
