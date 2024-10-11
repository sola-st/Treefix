# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
dt = np.dtype([("spam", np.str_, 16), ("eggs", np.float64, (2,))])
a = np.array([("spam", (8.0, 7.0)), ("eggs", (6.0, 5.0))], dtype=dt)
self.assertFalse(debug_data.has_inf_or_nan(self._dummy_datum, a))
