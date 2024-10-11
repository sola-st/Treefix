# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series([1, np.nan, 1, 1])
_, ax = self.plt.subplots()
ax = s.plot.pie(legend=True, ax=ax)
expected = ["0", "", "2", "3"]
result = [x.get_text() for x in ax.texts]
assert result == expected
