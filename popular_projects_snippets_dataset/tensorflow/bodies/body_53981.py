# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
a2 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
a3 = np.array([[10.0, 20.0, 30.0], [40.0, 50.0, 60.0]])
self.assertTrue(self._NDArrayNear(a1, a2, 1e-5))
self.assertFalse(self._NDArrayNear(a1, a3, 1e-5))
