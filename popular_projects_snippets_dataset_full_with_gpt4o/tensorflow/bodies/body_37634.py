# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
tensor = math_ops.range(10)
print_op = logging_ops.print_v2(tensor, name="print_name")
self.assertEqual(print_op.name, "print_name")
