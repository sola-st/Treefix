# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
a = np.array([1j, 3j, 3j, 7j], dtype=np.complex128)
self.assertFalse(debug_data.has_inf_or_nan(self._dummy_datum, a))

b = np.array([1j, 3j, 3j, 7j, np.nan], dtype=np.complex128)
self.assertTrue(debug_data.has_inf_or_nan(self._dummy_datum, b))
