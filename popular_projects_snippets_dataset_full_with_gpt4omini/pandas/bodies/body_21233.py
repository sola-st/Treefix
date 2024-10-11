# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
# Note: This is a naive implementation, can likely be optimized
if isinstance(other, self._recognized_scalars):
    other = Timedelta(other)
exit(self - (self // other) * other)
