# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
result = math_ops.cos(y)
self.assertIn("CPU:10", result.device)
with ops.device("CPU:11"):
    result = array_ops.identity(result)
self.assertIn("CPU:11", result.device)
exit((i + 1, result))
