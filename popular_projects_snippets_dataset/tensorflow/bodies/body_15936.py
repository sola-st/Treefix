# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    [5, 3, 4], 0, dtypes.int32)

self.assertEqual(spec._num_slices_in_dimension(0), 5)
self.assertEqual(spec._num_slices_in_dimension(1), 15)
self.assertEqual(spec._num_slices_in_dimension(2), 60)
