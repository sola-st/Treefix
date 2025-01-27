# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt = MaskedTensorV1([1.0, 2.0, 3.0, 4.0], [True, True, False, True])
mt_spec = MaskedTensorV1.Spec.from_value(mt)

expected_values_spec = tensor_spec.TensorSpec([4], dtypes.float32)
expected_mask_spec = tensor_spec.TensorSpec([4], dtypes.bool)
self.assertEqual(mt_spec.values, expected_values_spec)
self.assertEqual(mt_spec.mask, expected_mask_spec)
