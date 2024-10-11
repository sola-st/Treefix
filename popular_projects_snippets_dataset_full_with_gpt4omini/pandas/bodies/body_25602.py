# Extracted from ./data/repos/pandas/pandas/util/_doctools.py
"""
        Calculate appropriate figure size based on left and right data.
        """
if vertical:
    # calculate required number of cells
    vcells = max(sum(self._shape(df)[0] for df in left), self._shape(right)[0])
    hcells = max(self._shape(df)[1] for df in left) + self._shape(right)[1]
else:
    vcells = max([self._shape(df)[0] for df in left] + [self._shape(right)[0]])
    hcells = sum([self._shape(df)[1] for df in left] + [self._shape(right)[1]])
exit((hcells, vcells))
