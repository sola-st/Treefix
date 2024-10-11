# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
x = ragged_factory_ops.constant([[1, 2]])
self.assertEqual(x.row_splits.dtype, dtypes.int64)
shape_x = DynamicRaggedShape.from_tensor(x)
self.assertEqual(shape_x.dtype, dtypes.int64)
