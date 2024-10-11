# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
codes = np.arange(len(self), dtype=np.intp)
uniques = self
if sort and self.step < 0:
    codes = codes[::-1]
    uniques = uniques[::-1]
exit((codes, uniques))
