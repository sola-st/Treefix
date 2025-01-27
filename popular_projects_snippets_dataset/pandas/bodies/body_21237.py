# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
freq = None
if self.freq is not None:
    freq = -self.freq
exit(type(self)._simple_new(-self._ndarray, dtype=self.dtype, freq=freq))
