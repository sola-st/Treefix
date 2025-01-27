# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
self.assertTrue(
    np.array_equal(self._Range(0, 5, 1), np.array([0, 1, 2, 3, 4])))
self.assertTrue(np.array_equal(self._Range(0, 5, 2), np.array([0, 2, 4])))
self.assertTrue(np.array_equal(self._Range(0, 6, 2), np.array([0, 2, 4])))
self.assertTrue(
    np.array_equal(self._Range(13, 32, 7), np.array([13, 20, 27])))
self.assertTrue(
    np.array_equal(
        self._Range(100, 500, 100), np.array([100, 200, 300, 400])))
self.assertEqual(math_ops.range(0, 5, 1).dtype, dtypes.int32)
