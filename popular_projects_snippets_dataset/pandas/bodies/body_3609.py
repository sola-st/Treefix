# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex_like.py
# https://github.com/pandas-dev/pandas/issues/31925
class MyDataFrame(DataFrame):
    pass

expected = DataFrame()
df = MyDataFrame()
result = df.reindex_like(expected)

tm.assert_frame_equal(result, expected)
