# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
desc = tensor_spec.TensorSpec([1], np.float32)
self.assertEqual(desc.dtype, dtypes.float32)
