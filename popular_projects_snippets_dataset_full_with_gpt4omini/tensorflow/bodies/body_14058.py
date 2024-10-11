# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
with self.assertRaises(TypeError):
    structured_tensor.StructuredTensor.Spec(
        _ragged_shape=DynamicRaggedShape.Spec(
            row_partitions=[],
            static_inner_shape=[],
            dtype=dtypes.int64),
        _fields=field_specs)
