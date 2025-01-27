# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
values_spec = tensor_spec.TensorSpec([4], dtypes.float32)
mask_spec = tensor_spec.TensorSpec([4], dtypes.bool)
mt_spec = MaskedTensorV1.Spec(values_spec, mask_spec)
self.assertEqual(copy.copy(mt_spec), mt_spec)
self.assertEqual(copy.deepcopy(mt_spec), mt_spec)
self.assertEqual(pickle.loads(pickle.dumps(mt_spec)), mt_spec)
