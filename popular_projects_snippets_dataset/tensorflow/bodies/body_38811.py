# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
value = ragged_factory_ops.constant([[1, 2], [3], [4, 5, 6]])
encoded = composite_tensor_ops.composite_tensor_to_variants(value)
proto = parsing_ops.SerializeTensor(tensor=encoded)
parsed = parsing_ops.ParseTensor(serialized=proto, out_type=dtypes.variant)
decoded = composite_tensor_ops.composite_tensor_from_variant(
    parsed, value._type_spec)
self.assertAllEqual(value, decoded)
