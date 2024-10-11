# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series(range(3))
_, ax = self.plt.subplots()
s.plot(kind=kind, ax=ax)
self.plt.close()
_, ax = self.plt.subplots()
getattr(s.plot, kind)()
self.plt.close()
