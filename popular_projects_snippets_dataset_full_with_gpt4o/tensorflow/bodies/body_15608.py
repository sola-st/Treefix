# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
self.assertRaises((ValueError, errors.InvalidArgumentError),
                  ragged_math_ops.range, [[0]], 5)
self.assertRaises((ValueError, errors.InvalidArgumentError),
                  ragged_math_ops.range, 0, [[5]])
self.assertRaises((ValueError, errors.InvalidArgumentError),
                  ragged_math_ops.range, 0, 5, [[0]])
self.assertRaises((ValueError, errors.InvalidArgumentError),
                  ragged_math_ops.range, [0], [1, 2])
