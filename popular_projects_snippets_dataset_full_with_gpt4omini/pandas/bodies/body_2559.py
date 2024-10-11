# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#47578
df = DataFrame({"a": [1, 2]})
df["a"] = DataFrame({"a": [10, 11]}, index=[1, 2])
expected = DataFrame({"a": [np.nan, 10]})
tm.assert_frame_equal(df, expected)

df = DataFrame({"a": [1, 2]})
df.isetitem(0, DataFrame({"a": [10, 11]}, index=[1, 2]))
tm.assert_frame_equal(df, expected)
