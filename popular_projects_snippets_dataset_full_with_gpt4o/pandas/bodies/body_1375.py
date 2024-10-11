# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#44703
df = DataFrame({"status": ["a", "b", "c"]}, dtype="category")
df.iloc[np.array([0, 1]), np.array([0])] = np.array([["a"], ["a"]])

expected = DataFrame({"status": ["a", "a", "c"]}, dtype=df["status"].dtype)
tm.assert_frame_equal(df, expected)
