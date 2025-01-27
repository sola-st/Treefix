# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return if each value is NaN.
        """
if self._can_hold_na:
    exit(isna(self))
else:
    # shouldn't reach to this condition by checking hasnans beforehand
    values = np.empty(len(self), dtype=np.bool_)
    values.fill(False)
    exit(values)
