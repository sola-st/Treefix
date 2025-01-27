# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 11559
df = tm.SubclassedDataFrame(
    {"X": [1, 2, 3], "Y": [4, 5, 6], "Z": [7, 8, 9]}, index=["a", "b", "c"]
)
res = df.loc[:, "X"]
exp = tm.SubclassedSeries([1, 2, 3], index=list("abc"), name="X")
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)

res = df.iloc[:, 1]
exp = tm.SubclassedSeries([4, 5, 6], index=list("abc"), name="Y")
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)

res = df.loc[:, "Z"]
exp = tm.SubclassedSeries([7, 8, 9], index=list("abc"), name="Z")
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)

res = df.loc["a", :]
exp = tm.SubclassedSeries([1, 4, 7], index=list("XYZ"), name="a")
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)

res = df.iloc[1, :]
exp = tm.SubclassedSeries([2, 5, 8], index=list("XYZ"), name="b")
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)

res = df.loc["c", :]
exp = tm.SubclassedSeries([3, 6, 9], index=list("XYZ"), name="c")
tm.assert_series_equal(res, exp)
assert isinstance(res, tm.SubclassedSeries)
