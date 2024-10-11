# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
struct = StructuredTensor.from_fields(fields, shape)
spec = StructuredTensor.Spec(_ragged_shape=DynamicRaggedShape.Spec(
    row_partitions=[],
    static_inner_shape=shape,
    dtype=dtypes.int64), _fields=field_specs)
actual_components = spec._to_components(struct)
rt_reconstructed = spec._from_components(actual_components)
self.assertAllEqual(struct, rt_reconstructed)
