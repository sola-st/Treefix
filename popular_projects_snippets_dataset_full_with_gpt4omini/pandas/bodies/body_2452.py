# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#45621
df = DataFrame(columns=["b"], index=Index([], name="a"))
df.loc[0] = 1
expected = DataFrame({"b": [1]}, index=Index([0], name="a"))
tm.assert_frame_equal(df, expected)
