# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
self.assertTrue(
    np.array_equal(self._Range(5, -1, -1), np.array([5, 4, 3, 2, 1, 0])))
self.assertTrue(
    np.allclose(self._Range(2.5, 0, -0.5), np.array([2.5, 2, 1.5, 1, 0.5])))
self.assertTrue(
    np.array_equal(self._Range(-5, -10, -3), np.array([-5, -8])))
