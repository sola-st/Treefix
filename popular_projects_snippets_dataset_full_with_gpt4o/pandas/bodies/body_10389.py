# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 9807
# Check transform dtype output is preserved
df = DataFrame([[1, 3], [2, 3]])
result = df.groupby(1).transform("mean")
expected = DataFrame([[1.5], [1.5]])
tm.assert_frame_equal(result, expected)
