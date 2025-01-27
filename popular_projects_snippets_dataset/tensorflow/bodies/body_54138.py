# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
self.assertEqual(st_spec._flat_tensor_specs,
                 [tensor_spec.TensorSpec(None, dtypes.variant)])
