# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
values_spec = tensor_spec.TensorSpec([4], dtypes.float32)
mask_spec = tensor_spec.TensorSpec([4], dtypes.bool)
mt_spec = MaskedTensorV1.Spec(values_spec, mask_spec)
self.assertEqual(mt_spec.values, values_spec)
self.assertEqual(mt_spec.mask, mask_spec)

mt = MaskedTensorV1([1.0, 2.0, 3.0, 4.0], [True, True, False, True])
self.assertEqual(mt._type_spec, mt_spec)
