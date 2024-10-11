# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command(
    "print_tensor", [tensor_name, "--ranges", "[-inf, 0.0]", "-s"],
    screen_info={"cols": 80})

self.assertEqual([
    "Tensor \"%s:DebugIdentity\": " % tensor_name +
    "Highlighted([-inf, 0.0]): 1 of 2 element(s) (50.00%)",
    "  dtype: float64",
    "  shape: (2, 1)",
    "",
    "Numeric summary:",
    "| - + | total |",
    "| 1 1 |     2 |",
    "|  min  max mean  std |",
    "| -2.0  7.0  2.5  4.5 |",
    "",
    "array([[ 7.],",
    "       [-2.]])",
], out.lines)

self.assertIn("tensor_metadata", out.annotations)
self.assertIn(10, out.annotations)
self.assertIn(11, out.annotations)
self.assertEqual([(8, 11, "bold")], out.font_attr_segs[11])
