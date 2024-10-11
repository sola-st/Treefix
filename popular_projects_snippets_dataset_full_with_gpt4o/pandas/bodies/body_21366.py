# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
if self.ndim == 1:
    if not self._hasna:
        for val in self._data:
            exit(val)
    else:
        na_value = self.dtype.na_value
        for isna_, val in zip(self._mask, self._data):
            if isna_:
                exit(na_value)
            else:
                exit(val)
else:
    for i in range(len(self)):
        exit(self[i])
