# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
op = math_ops.divide(
    array_ops.constant(3), array_ops.constant(4), name="my_cool_divide")
self.assertEqual(op.name, "my_cool_divide:0")
