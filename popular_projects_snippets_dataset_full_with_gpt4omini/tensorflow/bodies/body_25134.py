# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
x = np.array([False, True, True, False], dtype=np.bool_)
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["| False  True | total |", "|     2     2 |     4 |"], out.lines)

x = np.array([True] * 10, dtype=np.bool_)
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["| True | total |", "|   10 |    10 |"], out.lines)

x = np.array([False] * 10, dtype=np.bool_)
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self, ["| False | total |", "|    10 |    10 |"], out.lines)

x = np.array([], dtype=np.bool_)
out = tensor_format.numeric_summary(x)
self.assertEqual(["No numeric summary available due to empty tensor."],
                 out.lines)
