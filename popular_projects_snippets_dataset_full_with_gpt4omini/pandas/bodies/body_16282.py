# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
left = Series(["a", "b", "c"], dtype=CategoricalDtype(["a", "b"]))
right = Series(Categorical(["a", "b", np.nan], categories=["a", "b"]))
tm.assert_series_equal(left, right)
