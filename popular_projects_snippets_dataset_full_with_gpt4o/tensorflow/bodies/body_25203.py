# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command(
    "eval", ["np.matmul(`%s`, `%s`.T)" % (tensor_name, tensor_name)],
    screen_info={"cols": 80})

cli_test_utils.assert_lines_equal_ignoring_whitespace(
    self,
    ["Tensor \"from eval of expression "
     "'np.matmul(`simple_mul_add/matmul:0`, "
     "`simple_mul_add/matmul:0`.T)'\":",
     "  dtype: float64",
     "  shape: (2, 2)",
     "",
     "Numeric summary:",
     "| - + | total |",
     "| 2 2 |     4 |",
     "|           min           max          mean           std |"],
    out.lines[:8])
cli_test_utils.assert_array_lines_close(
    self, [-14.0, 49.0, 6.25, 25.7524270701], out.lines[8:9])
cli_test_utils.assert_array_lines_close(
    self, [[49.0, -14.0], [-14.0, 4.0]], out.lines[10:])
