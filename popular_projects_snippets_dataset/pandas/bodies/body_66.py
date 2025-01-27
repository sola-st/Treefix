# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 20714 bug fixed in: GH 24275
s = Series(series, dtype="category")
result = s.apply(lambda x: x.split("-")[0])
result = result.astype(object)
expected = Series(["1", "1", np.NaN], dtype="category")
expected = expected.astype(object)
tm.assert_series_equal(result, expected)
