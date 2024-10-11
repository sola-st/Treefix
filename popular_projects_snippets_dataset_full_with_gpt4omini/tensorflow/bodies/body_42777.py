# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
compatibility_date = self._compatibility_date()
one_day_after = self._n_days_after(1)

class DummyError(Exception):
    pass

try:
    with compat.forward_compatibility_horizon(*one_day_after):
        raise DummyError()
except DummyError:
    pass  # silence DummyError

# After exiting context manager, value should be reset.
self.assertFalse(compat.forward_compatible(*compatibility_date))
