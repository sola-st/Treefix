# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = dynamic_ragged_shape.DynamicRaggedShape.Spec._from_tensor_shape(
    shape=tensor_shape.TensorShape([5, None, 7, 4, 2, 5]),
    num_row_partitions=2,
    dtype=dtypes.int32)

self.assertEqual(spec._dimension(0), 5)
self.assertIsNone(spec._dimension(1))
self.assertEqual(spec._dimension(2), 7)
self.assertEqual(spec._dimension(3), 4)
self.assertEqual(spec._dimension(4), 2)
self.assertEqual(spec._dimension(5), 5)
