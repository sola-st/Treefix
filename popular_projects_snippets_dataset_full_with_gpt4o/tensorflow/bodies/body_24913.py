# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
a = np.array([np.inf, np.inf, 7.0])
self.assertTrue(debug_data.has_inf_or_nan(self._dummy_datum, a))
