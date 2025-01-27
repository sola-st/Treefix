# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
a = np.array([1, 3, 3, 7], dtype=np.int16)
self.assertFalse(debug_data.has_inf_or_nan(self._dummy_datum, a))
