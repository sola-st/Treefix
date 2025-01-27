# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(np.arange(12).reshape(3, 4))
result = df[lst]
expected = df.loc[df.index[lst]]
tm.assert_frame_equal(result, expected)
