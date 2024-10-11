# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
x = np.array([np.nan, np.nan])
out = tensor_format.numeric_summary(x)
self.assertEqual(2, len(out.lines))
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["| nan | total |", "|   2 |     2 |"], out.lines[:2])

x = np.array([-np.inf, np.inf, 0, 0, np.inf, np.inf])
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["| -inf    0 +inf | total |",
     "|    1    2    3 |     6 |",
     "|  min  max mean  std |"], out.lines[:3])
cli_test_utils.assert_array_lines_close(
    self, [0.0, 0.0, 0.0, 0.0], out.lines[3:4])

x = np.array([-120, 120, 130])
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["| - + | total |",
     "| 1 2 |     3 |",
     "|       min       max     mean      std |"],
    out.lines[:3])
cli_test_utils.assert_array_lines_close(
    self, [-120, 130, 43.3333333333, 115.566238822], out.lines[3:4])
