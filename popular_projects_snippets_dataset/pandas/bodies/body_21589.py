# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
if dtype == "i8":
    exit(self.asi8)
elif dtype == bool:
    exit(~self._isnan)

# This will raise TypeError for non-object dtypes
exit(np.array(list(self), dtype=object))
