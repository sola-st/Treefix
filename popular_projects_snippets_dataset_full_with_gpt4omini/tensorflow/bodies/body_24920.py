# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
"""isnan and isinf are not applicable to strings."""

a = np.array(["s", "p", "a", "m"])
self.assertFalse(debug_data.has_inf_or_nan(self._dummy_datum, a))
