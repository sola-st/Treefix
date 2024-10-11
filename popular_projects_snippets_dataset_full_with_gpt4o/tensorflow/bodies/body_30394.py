# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
self._compare(np.inf, np.float32, np.inf, False)
self._compare(np.inf, np.float64, np.inf, False)
self._compare(-np.inf, np.float32, -np.inf, False)
self._compare(-np.inf, np.float64, -np.inf, False)
self.assertAllEqual(np.isnan(self._cast(np.nan, np.float32, False)), True)
self.assertAllEqual(np.isnan(self._cast(np.nan, np.float64, False)), True)

self._compare(np.inf, np.float32, np.inf, True)
self._compare(np.inf, np.float64, np.inf, True)
self._compare(-np.inf, np.float32, -np.inf, True)
self._compare(-np.inf, np.float64, -np.inf, True)
self.assertAllEqual(np.isnan(self._cast(np.nan, np.float32, True)), True)
self.assertAllEqual(np.isnan(self._cast(np.nan, np.float64, True)), True)
