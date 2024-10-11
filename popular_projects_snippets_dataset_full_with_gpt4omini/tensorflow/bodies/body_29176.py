# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
tf_value = tf_value_fn()
opt = optional_ops.Optional.from_value(tf_value)

self.assertTrue(
    structure.are_compatible(opt.element_spec, expected_value_structure))

opt_structure = structure.type_spec_from_value(opt)
self.assertIsInstance(opt_structure, optional_ops.OptionalSpec)
self.assertTrue(structure.are_compatible(opt_structure, opt_structure))
self.assertTrue(
    structure.are_compatible(opt_structure._element_spec,
                             expected_value_structure))
self.assertEqual([dtypes.variant],
                 structure.get_flat_tensor_types(opt_structure))
self.assertEqual([tensor_shape.TensorShape([])],
                 structure.get_flat_tensor_shapes(opt_structure))

# All OptionalSpec objects are not compatible with a non-optional
# value.
non_optional_structure = structure.type_spec_from_value(
    constant_op.constant(42.0))
self.assertFalse(opt_structure.is_compatible_with(non_optional_structure))

# Assert that the optional survives a round-trip via _from_tensor_list()
# and _to_tensor_list().
round_trip_opt = opt_structure._from_tensor_list(
    opt_structure._to_tensor_list(opt))
if isinstance(tf_value, optional_ops.Optional):
    self.assertValuesEqual(
        self.evaluate(tf_value.get_value()),
        self.evaluate(round_trip_opt.get_value().get_value()))
else:
    self.assertValuesEqual(
        self.evaluate(tf_value), self.evaluate(round_trip_opt.get_value()))
