# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
a = TwoComposites(
    ragged_factory_ops.constant([[1, 2], [3]]),
    ragged_factory_ops.constant([[5], [6, 7, 8]]))
a_spec = type_spec.type_spec_from_value(a)
flat_specs = a_spec._flat_tensor_specs
self.assertEqual(flat_specs, [
    tensor_spec.TensorSpec(None, dtypes.variant),
    tensor_spec.TensorSpec(None, dtypes.variant)
])
