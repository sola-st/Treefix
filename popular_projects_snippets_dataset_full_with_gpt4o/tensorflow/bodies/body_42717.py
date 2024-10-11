# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
# Unless explicitly specified, float64->float32
t = _create_tensor(3.0)
self.assertEqual(dtypes.float32, t.dtype)
t = _create_tensor(3.0, dtype=dtypes.float64)
self.assertEqual(dtypes.float64, t.dtype)
