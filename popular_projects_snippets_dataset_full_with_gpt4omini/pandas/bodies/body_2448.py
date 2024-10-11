# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#43422
df = DataFrame(columns=["a", "b"], dtype=object)
df.loc[0] = {"a": np.zeros((2,)), "b": np.zeros((2, 2))}
expected = DataFrame({"a": [np.zeros((2,))], "b": [np.zeros((2, 2))]})
tm.assert_frame_equal(df, expected)
