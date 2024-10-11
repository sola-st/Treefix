# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH28172
s = Series(range(10), index=[f"P{i:02d}" for i in range(10)])
ax = s.plot.bar(xticks=range(0, 11, 2))
exp = np.array(list(range(0, 11, 2)))
tm.assert_numpy_array_equal(exp, ax.get_xticks())
