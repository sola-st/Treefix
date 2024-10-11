# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# https://github.com/pandas-dev/pandas/issues/40258
expected = DataFrame({"a": [1, 4, 2, 5, 3, 6]})
result = expected.sort_values(by=[])
tm.assert_frame_equal(result, expected)
assert result is not expected
