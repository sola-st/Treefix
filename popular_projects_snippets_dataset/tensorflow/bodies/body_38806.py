# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
value = value_factory()

encoded = composite_tensor_ops.composite_tensor_to_variants(value)
self.assertEqual(encoded.dtype, dtypes.variant)
self.assertEqual(encoded.shape.rank, 0)

decoded = composite_tensor_ops.composite_tensor_from_variant(
    encoded, value._type_spec)
self.assertTrue(value._type_spec.is_compatible_with(decoded._type_spec))
value_components = nest.flatten(value, expand_composites=True)
decoded_components = nest.flatten(decoded, expand_composites=True)
self.assertLen(value_components, len(decoded_components))
for v, d in zip(value_components, decoded_components):
    self.assertAllEqual(v, d)
