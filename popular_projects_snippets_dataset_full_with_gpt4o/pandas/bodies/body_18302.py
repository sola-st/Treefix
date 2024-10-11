# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_categorical.py
cat = Series(Categorical(["a", "b", "c", np.nan]))
expected = Series([True, True, True, False])
result = cat == cat
tm.assert_series_equal(result, expected)
