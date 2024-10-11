# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py

df = DataFrame({"A": ["foo", 2], "B": [True, False]}).astype(object)
df._consolidate_inplace()
df["C"] = Series([True, True])

# Categorical of bools is _not_ considered booly
df["D"] = df["C"].astype("category")

# The underlying bug is in DataFrame._get_bool_data, so we check
#  that while we're here
res = df._get_bool_data()
expected = df[["C"]]
tm.assert_frame_equal(res, expected)

res = df.all(bool_only=True, axis=0)
expected = Series([True], index=["C"])
tm.assert_series_equal(res, expected)

# operating on a subset of columns should not produce a _larger_ Series
res = df[["B", "C"]].all(bool_only=True, axis=0)
tm.assert_series_equal(res, expected)

assert df.all(bool_only=True, axis=None)

res = df.any(bool_only=True, axis=0)
expected = Series([True], index=["C"])
tm.assert_series_equal(res, expected)

# operating on a subset of columns should not produce a _larger_ Series
res = df[["C"]].any(bool_only=True, axis=0)
tm.assert_series_equal(res, expected)

assert df.any(bool_only=True, axis=None)
