# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# GH 42295

df = DataFrame({"a": [1.0, 2.0], "b": [3, np.nan]})
expected = df.copy()
result = df.where(pd.notnull(df), None)
# make sure dtypes don't change
tm.assert_frame_equal(expected, result)
