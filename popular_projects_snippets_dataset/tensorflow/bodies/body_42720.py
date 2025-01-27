# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(3)
self.assertEqual(dtypes.int32, t.dtype)
t = _create_tensor(3, dtype=dtypes.int64)
self.assertEqual(dtypes.int64, t.dtype)
t = _create_tensor(2**33)
self.assertEqual(dtypes.int64, t.dtype)
