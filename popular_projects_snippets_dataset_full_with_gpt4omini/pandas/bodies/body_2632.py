# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 12983
df = tm.SubclassedDataFrame({"a": [1, 3, 5], "b": [1, 3, 5]}, index=list("ACE"))
s = tm.SubclassedSeries([1, 2, 4], index=list("ABD"), name="x")

# frame + series
res1, res2 = df.align(s, axis=0)
exp1 = tm.SubclassedDataFrame(
    {"a": [1, np.nan, 3, np.nan, 5], "b": [1, np.nan, 3, np.nan, 5]},
    index=list("ABCDE"),
)
# name is lost when
exp2 = tm.SubclassedSeries(
    [1, 2, np.nan, 4, np.nan], index=list("ABCDE"), name="x"
)

assert isinstance(res1, tm.SubclassedDataFrame)
tm.assert_frame_equal(res1, exp1)
assert isinstance(res2, tm.SubclassedSeries)
tm.assert_series_equal(res2, exp2)

# series + frame
res1, res2 = s.align(df)
assert isinstance(res1, tm.SubclassedSeries)
tm.assert_series_equal(res1, exp2)
assert isinstance(res2, tm.SubclassedDataFrame)
tm.assert_frame_equal(res2, exp1)
