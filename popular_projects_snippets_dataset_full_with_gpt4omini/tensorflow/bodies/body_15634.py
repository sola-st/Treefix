# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
tensor = [[6.0, 9.0, 6.0], [60.0, 90.0, 60.0]]
expected = [2., 200.]
reduced = ragged_math_ops.reduce_variance(tensor, axis=1)
self.assertAllEqual(reduced, expected)
