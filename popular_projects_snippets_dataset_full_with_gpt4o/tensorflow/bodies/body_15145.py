# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
self.assertEqual(rt_spec._flat_tensor_specs,
                 [tensor_spec.TensorSpec(None, dtypes.variant)])
