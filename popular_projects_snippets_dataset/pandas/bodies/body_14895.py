# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
x = Series(np.random.randn(2))
_, ax = self.plt.subplots()
msg = (
    "Cannot pass 'style' string with a color symbol and 'color' keyword "
    "argument. Please use one or the other or pass 'style' without a color "
    "symbol"
)
with pytest.raises(ValueError, match=msg):
    x.plot(style="k--", color="k", ax=ax)
