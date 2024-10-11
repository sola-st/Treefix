# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)
with self.assertRaises(ValueError):
    print_op = logging_ops.print_v2(
        tensor, output_stream="unknown")
    self.evaluate(print_op)
