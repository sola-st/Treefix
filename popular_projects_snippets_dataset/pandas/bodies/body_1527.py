# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
df = DataFrame({"A": pd.array([0, 0], dtype=SparseDtype("int64"))})
result = df.loc[[0, 1]]
tm.assert_frame_equal(result, df)
