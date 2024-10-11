# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
desc = tensor_spec.TensorSpec([1, 5], dtypes.float32, "test")
self.assertEqual(pickle.loads(pickle.dumps(desc)), desc)
