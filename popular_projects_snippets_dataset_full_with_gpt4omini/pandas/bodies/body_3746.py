# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# GH#41965
df = DataFrame([[1, 2], [3, 4]], columns=pd.RangeIndex(0, 2))
expected = df.copy()
result = df.dropna(axis=axis)
tm.assert_frame_equal(result, expected, check_index_type=True)
