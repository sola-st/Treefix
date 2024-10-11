# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 18480
d = {1: "a", value: "b", float("nan"): "c", 4: "d"}
result = Series(d).sort_values()
expected = Series(["a", "b", "c", "d"], index=[1, value, np.nan, 4])
tm.assert_series_equal(result, expected)

# MultiIndex:
d = {(1, 1): "a", (2, np.nan): "b", (3, value): "c"}
result = Series(d).sort_values()
expected = Series(
    ["a", "b", "c"], index=Index([(1, 1), (2, np.nan), (3, value)])
)
tm.assert_series_equal(result, expected)
