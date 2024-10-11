# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
x = np.array([-3] * 50 + [3] * 200 + [0], dtype=np.int32)
out = tensor_format.numeric_summary(x)
cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["|   -   0   + | total |",
     "|  50   1 200 |   251 |",
     "|      min     max    mean     std |"],
    out.lines[:3])
cli_test_utils.assert_array_lines_close(
    self, [-3, 3, 1.79282868526, 2.39789673081], out.lines[3:4])
