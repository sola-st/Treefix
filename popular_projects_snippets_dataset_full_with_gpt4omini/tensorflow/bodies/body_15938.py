# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = DynamicRaggedShape.Spec._from_tensor_shape(
    shape=tensor_shape.TensorShape([5, 3, 7, 4, None, 5]),
    num_row_partitions=2,
    dtype=dtypes.int32)
actual = spec.with_dtype(dtypes.int64)
self.assertEqual(actual.dtype, dtypes.int64)
self.assertEqual(actual._row_partitions[0].dtype, dtypes.int64)
self.assertEqual(actual._row_partitions[1].dtype, dtypes.int64)
