# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# https://github.com/pandas-dev/pandas/issues/17962
# Checks that method runs for non string column names
left = DataFrame(
    {0: [1, 0, 1, 0], 1: [0, 1, 0, 0], 2: [0, 0, 2, 0], 3: [1, 0, 0, 3]}
)

right = left.astype(float)
expected = left
result = merge(left, right)
tm.assert_frame_equal(expected, result)
