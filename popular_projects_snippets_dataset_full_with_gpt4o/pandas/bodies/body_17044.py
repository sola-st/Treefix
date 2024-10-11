# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 43595
keys = ["e", "e"]
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
result = concat([df, df], axis=1, keys=keys)
expected_values = [[1, 4, 1, 4], [2, 5, 2, 5], [3, 6, 3, 6]]
expected_columns = MultiIndex.from_tuples(
    [(keys[0], "a"), (keys[0], "b"), (keys[1], "a"), (keys[1], "b")]
)
expected = DataFrame(expected_values, columns=expected_columns)
with catch_warnings():
    # result.columns not sorted, resulting in performance warning
    simplefilter("ignore", PerformanceWarning)
    tm.assert_frame_equal(result, expected)
