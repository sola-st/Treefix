# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
x = MaskedTensorV2([4, 5], [True, False])
spec = type_spec.type_spec_from_value(x)
flat_specs = spec._flat_tensor_specs
self.assertEqual(flat_specs, [
    tensor_spec.TensorSpec(shape=(2,), dtype=dtypes.int32, name=None),
    tensor_spec.TensorSpec(shape=(2,), dtype=dtypes.bool, name=None)
])
