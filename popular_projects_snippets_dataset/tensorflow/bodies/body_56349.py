# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.TensorSpec([1], np.float32)
self.assertEqual(spec._flat_tensor_specs, [spec])
