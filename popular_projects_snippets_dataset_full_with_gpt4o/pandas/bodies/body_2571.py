# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#16823 / GH#17894
df = DataFrame()
df["foo"] = 1
expected = DataFrame(columns=["foo"]).astype(np.int64)
tm.assert_frame_equal(df, expected)
