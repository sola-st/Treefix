# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#40885
df = DataFrame({"a": [1, 2], "b": [3, 4], "c": "a"})
expected = df.copy()
indexer = Series([False, False], name="c")
df.loc[indexer, ["b"]] = DataFrame({"b": [5, 6]}, index=[0, 1])
tm.assert_frame_equal(df, expected)
