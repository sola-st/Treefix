# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# Test for issue GH#11859

df = DataFrame()
df2 = df[df > 0]
tm.assert_frame_equal(df, df2)
