# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_sort.py
# GH-4588
# We catch TypeErrors from sorting internally and do not re-raise.
df = DataFrame({1: [1, 2], "a": [3, 4]}, columns=[1, "a"])
expected = DataFrame({1: [1, 2, 1, 2], "a": [3, 4, 3, 4]}, columns=[1, "a"])
result = pd.concat([df, df], ignore_index=True, sort=True)
tm.assert_frame_equal(result, expected)
