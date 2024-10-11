# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
compatibility_date = self._compatibility_date()
one_day_after = self._n_days_after(1)
with compat.forward_compatibility_horizon(*one_day_after):
    self.assertTrue(compat.forward_compatible(*compatibility_date))
    self.assertFalse(compat.forward_compatible(*one_day_after))

# After exiting context manager, value should be reset.
self.assertFalse(compat.forward_compatible(*compatibility_date))
