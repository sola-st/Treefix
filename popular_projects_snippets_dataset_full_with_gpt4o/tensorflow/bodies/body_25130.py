# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
x = np.array([np.nan, np.nan, -np.inf, np.inf, np.inf, np.inf, -2, -3, -4,
              0, 1, 2, 2, 2, 2, 0, 0, 0, np.inf, np.inf, np.inf])
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["|  nan -inf    -    0    + +inf | total |",
     "|    2    1    3    4    5    6 |    21 |",
     "|     min     max    mean    std |"], out.lines[:3])
cli_test_utils.assert_array_lines_close(
    self, [-4.0, 2.0, 0.0, 1.95789002075], out.lines[3:4])
