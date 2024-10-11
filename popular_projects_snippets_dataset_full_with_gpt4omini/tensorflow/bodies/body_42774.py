# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
compatibility_date = self._compatibility_date()
one_day_before = self._n_days_after(-1)
self.assertTrue(compat.forward_compatible(*one_day_before))
self.assertFalse(compat.forward_compatible(*compatibility_date))
