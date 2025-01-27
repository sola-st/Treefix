# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 27472
df = DataFrame({"a": [0, 0, 0, 1, 1, 1], "b": range(6)})
grp = df.groupby(np.repeat([0, 1], 3))

result = grp.cumcount()
expected = Series([0, 1, 2, 0, 1, 2])
tm.assert_series_equal(result, expected)

result = grp.transform("cumcount")
tm.assert_series_equal(result, expected)
