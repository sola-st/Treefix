# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
self.assertTrue(
    np.allclose(self._Range(0, 2, 0.5), np.array([0, 0.5, 1, 1.5])))
self.assertTrue(np.allclose(self._Range(0, 5, 2.5), np.array([0, 2.5])))
self.assertTrue(
    np.allclose(self._Range(0, 3, 0.9), np.array([0, 0.9, 1.8, 2.7])))
self.assertTrue(
    np.allclose(
        self._Range(100., 500., 100.), np.array([100, 200, 300, 400])))
self.assertEqual(math_ops.range(0., 5., 1.).dtype, dtypes.float32)
