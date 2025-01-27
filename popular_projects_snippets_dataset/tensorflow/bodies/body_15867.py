# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = constant_op.constant([[4]])
b = RaggedTensor.from_row_splits([[2], [3], [4], [5]], [0, 3, 4])
b = b.with_row_splits_dtype(dtype)
c = a + b
self.assertEqual(c.row_splits.dtype, dtype)
d = b + a
self.assertEqual(d.row_splits.dtype, dtype)
