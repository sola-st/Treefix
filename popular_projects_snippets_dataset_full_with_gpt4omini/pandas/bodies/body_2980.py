# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#28813 .diff() should work for sparse dataframes as well
sparse_df = DataFrame([[0, 1], [1, 0]], dtype="Sparse[int]")

result = sparse_df.diff()
expected = DataFrame(
    [[np.nan, np.nan], [1.0, -1.0]], dtype=pd.SparseDtype("float", 0.0)
)

tm.assert_frame_equal(result, expected)
