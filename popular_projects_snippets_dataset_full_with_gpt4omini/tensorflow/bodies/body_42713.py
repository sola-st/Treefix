# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
expected = np.array([[1.0, 2.0], [3.0, 4.0]], np.float32)
actual = _create_tensor([[1.0, 2.0], [3.0, 4.0]])
self.assertAllEqual(expected, actual)
self.assertEqual(np.float32, actual.dtype)
self.assertEqual(dtypes.float32, actual.dtype)
self.assertAllEqual([2, 2], actual.shape.as_list())
