# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
self.assertEqual(dtypes.float64, _create_tensor(np.float64()).dtype)  # pylint: disable=no-value-for-parameter
self.assertEqual(dtypes.float32, _create_tensor(np.float32()).dtype)  # pylint: disable=no-value-for-parameter
self.assertEqual(dtypes.float16, _create_tensor(np.float16()).dtype)  # pylint: disable=no-value-for-parameter
self.assertEqual(dtypes.float32, _create_tensor(0.0).dtype)
