# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
tensor = [[1.0, 2.0, 2.0, 1.0], [10.0, 20.0, 20.0, 10.0]]
expected = [0.5, 5.]
reduced = ragged_math_ops.reduce_std(tensor, axis=1)
self.assertAllEqual(reduced, expected)
