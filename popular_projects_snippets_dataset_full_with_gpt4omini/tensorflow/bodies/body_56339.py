# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec_1 = tensor_spec.TensorSpec((1, 2), dtypes.int32)
spec_2 = tensor_spec.TensorSpec.from_spec(spec_1)
self.assertEqual(spec_1, spec_2)
