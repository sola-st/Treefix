# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
spec1_fields = dict(a=T_1_2_3_4)
spec1 = StructuredTensor.Spec(
    _ragged_shape=DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=tensor_shape.TensorShape([1, 2, 3]),
        dtype=dtypes.int64),
    _fields=spec1_fields)
self.assertEqual(spec1._shape, (1, 2, 3))
self.assertEqual(spec1._field_specs, spec1_fields)

spec2_fields = dict(a=T_1_2, b=T_1_2_8, c=R_1_N, d=R_1_N_N, s=spec1)
spec2 = StructuredTensor.Spec(
    _ragged_shape=DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=tensor_shape.TensorShape([1, 2]),
        dtype=dtypes.int64),
    _fields=spec2_fields)
self.assertEqual(spec2._shape, (1, 2))
self.assertEqual(spec2._field_specs, spec2_fields)
