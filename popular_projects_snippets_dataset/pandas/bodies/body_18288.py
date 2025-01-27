# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
ser = Series(["foo", "bar", "baz", np.nan])
result = "prefix_" + ser
expected = Series(["prefix_foo", "prefix_bar", "prefix_baz", np.nan])
tm.assert_series_equal(result, expected)

result = ser + "_suffix"
expected = Series(["foo_suffix", "bar_suffix", "baz_suffix", np.nan])
tm.assert_series_equal(result, expected)
