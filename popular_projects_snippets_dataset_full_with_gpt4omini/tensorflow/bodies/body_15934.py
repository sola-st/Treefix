# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    shape=tensor_shape.TensorShape([5, 3, 7, 4, None, 5]),
    num_row_partitions=2,
    dtype=dtypes.int32)

self.assertEqual(spec._num_slices_in_dimension(0), 5)
self.assertEqual(spec._num_slices_in_dimension(1), 5 * 3)
self.assertEqual(spec._num_slices_in_dimension(2), 5 * 3 * 7)
self.assertEqual(spec._num_slices_in_dimension(3), 5 * 3 * 7 * 4)
self.assertIsNone(spec._num_slices_in_dimension(4))
self.assertIsNone(spec._num_slices_in_dimension(5))
self.assertIsNone(spec._num_slices_in_dimension(-2))
