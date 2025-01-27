# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
tensor = [[1.0, 2.0, 3.0], [10.0, 20.0, 30.0]]
expected = [2.0, 20.0]
reduced = ragged_math_ops.reduce_mean(tensor, axis=1)
self.assertAllEqual(reduced, expected)
