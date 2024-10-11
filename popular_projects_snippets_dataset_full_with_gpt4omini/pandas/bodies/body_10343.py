# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH29645
expected = Series(["y"])
data = Series(
    [nulls_fixture, nulls_fixture, nulls_fixture, "y", nulls_fixture],
    index=[0, 0, 0, 0, 0],
).groupby(level=0)

if method == "nth":
    result = getattr(data, method)(3)
else:
    result = getattr(data, method)()

tm.assert_series_equal(result, expected)
