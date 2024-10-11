# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    shape=tensor_shape.TensorShape([5, None, 7, 4, 2, 5]),
    num_row_partitions=2,
    dtype=dtypes.int32)

self.assertEqual(spec.inner_rank, 4)
self.assertEqual(spec.num_row_partitions, 2)
self.assertEqual(spec.rank, 6)
