# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
spec = DynamicRaggedShape.Spec._from_tensor_shape(shape, num_row_partitions,
                                                  dtype)
self.assertDynamicRaggedShapeSpecEqual(spec, expected)
