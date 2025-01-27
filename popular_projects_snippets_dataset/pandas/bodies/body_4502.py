# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

items = [1, 2, 3, 1]
exp = Series(items).astype("category")
res = Series(items, dtype="category")
tm.assert_series_equal(res, exp)

items = ["a", "b", "c", "a"]
exp = Series(items).astype("category")
res = Series(items, dtype="category")
tm.assert_series_equal(res, exp)

# insert into frame with different index
# GH 8076
index = date_range("20000101", periods=3)
expected = Series(
    Categorical(values=[np.nan, np.nan, np.nan], categories=["a", "b", "c"])
)
expected.index = index

expected = DataFrame({"x": expected})
df = DataFrame({"x": Series(["a", "b", "c"], dtype="category")}, index=index)
tm.assert_frame_equal(df, expected)
