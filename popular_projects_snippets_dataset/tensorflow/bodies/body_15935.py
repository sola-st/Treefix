# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    shape=tensor_shape.TensorShape([5, 3, None, 2]),
    num_row_partitions=3,
    dtype=dtypes.int32)

self.assertEqual(spec._num_slices_in_dimension(0), 5)
self.assertEqual(spec._num_slices_in_dimension(1), 5 * 3)
self.assertIsNone(spec._num_slices_in_dimension(2))
self.assertIsNone(spec._num_slices_in_dimension(3))
