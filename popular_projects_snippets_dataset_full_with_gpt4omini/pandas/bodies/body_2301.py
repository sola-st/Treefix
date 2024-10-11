# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 10218
# test DataFrame.where with Series slicing
df = DataFrame({"a": range(3), "b": range(4, 7)})
result = df.where(df["a"] == 1)
expected = df[df["a"] == 1].reindex(df.index)
tm.assert_frame_equal(result, expected)
