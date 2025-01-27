# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
x = ragged_factory_ops.constant([[1, 2]])
self.assertEqual(x.row_splits.dtype, dtypes.int64)

y = math_ops.add(x, x)
self.assertEqual(y.row_splits.dtype, dtypes.int64)
