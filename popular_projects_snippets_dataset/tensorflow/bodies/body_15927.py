# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(error_type, error_regex):
    DynamicRaggedShape.Spec._from_tensor_shape(shape, num_row_partitions,
                                               dtype)
