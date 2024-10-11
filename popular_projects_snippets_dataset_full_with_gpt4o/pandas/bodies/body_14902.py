# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series(["a", "b", 1.0, 2])
_, ax = self.plt.subplots()
msg = "no numeric data to plot"
with pytest.raises(TypeError, match=msg):
    s.plot(kind=kind, ax=ax)
