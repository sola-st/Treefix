# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
spec1 = StructuredTensor.Spec(
    _ragged_shape=DynamicRaggedShape.Spec(
        row_partitions=[],
        static_inner_shape=[1, 2],
        dtype=dtypes.int64),
    _fields=dict(a=T_1_2))
self.assertEqual(spec1.value_type, StructuredTensor)
