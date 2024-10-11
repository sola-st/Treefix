# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 37593
df = DataFrame(columns=["a"], index=[0])
df.iloc[0, 0] = Series([1, 2, 3])
expected = DataFrame({"a": [Series([1, 2, 3])]}, columns=["a"], index=[0])
tm.assert_frame_equal(df, expected)
