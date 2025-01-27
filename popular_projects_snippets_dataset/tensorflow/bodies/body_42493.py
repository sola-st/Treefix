# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tensor_test.py
result = util.get_scalar_one()
self.assertIsInstance(result, np.ndarray)
self.assertAllEqual(result, 1.0)
