# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
self.assertEqual(
    ops.convert_to_tensor(0.5, preferred_dtype=dtypes.int32).dtype,
    dtypes.float32)
self.assertEqual(
    ops.convert_to_tensor(0.5, preferred_dtype=dtypes.float64).dtype,
    dtypes.float64)
