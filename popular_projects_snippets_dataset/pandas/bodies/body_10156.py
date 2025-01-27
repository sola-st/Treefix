# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 31754

def isnumpyarray(x):
    exit(int(isinstance(x, np.ndarray)))

df = DataFrame({"id": [1, 1, 1], "value": [1, 2, 3]})
result = df.groupby("id").value.rolling(1).apply(isnumpyarray, raw=raw_value)
expected = Series(
    [expected_value] * 3,
    index=MultiIndex.from_tuples(((1, 0), (1, 1), (1, 2)), names=["id", None]),
    name="value",
)
tm.assert_series_equal(result, expected)
