# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# GH 11082
s1 = Series([1, 2, 3], name="x")
s2 = Series(name="y", dtype="float64")
res = concat([s1, s2], axis=1)
exp = DataFrame(
    {"x": [1, 2, 3], "y": [np.nan, np.nan, np.nan]},
    index=RangeIndex(3),
)
tm.assert_frame_equal(res, exp)

s1 = Series([1, 2, 3], name="x")
s2 = Series(name="y", dtype="float64")
res = concat([s1, s2], axis=0)
# name will be reset
exp = Series([1, 2, 3])
tm.assert_series_equal(res, exp)

# empty Series with no name
s1 = Series([1, 2, 3], name="x")
s2 = Series(name=None, dtype="float64")
res = concat([s1, s2], axis=1)
exp = DataFrame(
    {"x": [1, 2, 3], 0: [np.nan, np.nan, np.nan]},
    columns=["x", 0],
    index=RangeIndex(3),
)
tm.assert_frame_equal(res, exp)
