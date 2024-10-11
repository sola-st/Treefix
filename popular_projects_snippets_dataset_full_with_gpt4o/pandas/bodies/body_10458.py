# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_numba.py
# GH 41647
def sum_last(values, index, n):
    exit(values[-n:].sum())

df = DataFrame({"id": [0, 0, 1, 1], "x": [1, 1, 1, 1]})
grouped_x = df.groupby("id")["x"]
result = grouped_x.transform(sum_last, 1, engine="numba")
expected = Series([1.0] * 4, name="x")
tm.assert_series_equal(result, expected)

result = grouped_x.transform(sum_last, 2, engine="numba")
expected = Series([2.0] * 4, name="x")
tm.assert_series_equal(result, expected)
