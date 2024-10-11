import unittest # pragma: no cover
import re # pragma: no cover

class MockedCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(it): # pragma: no cover
        if not hasattr(it, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockedSelf: # pragma: no cover
    def assertRaisesRegex(self, exc_type, regex, *args, **kwargs): # pragma: no cover
        context = unittest.TestCase() # pragma: no cover
        with context.assertRaisesRegex(exc_type, regex): # pragma: no cover
            return context # pragma: no cover
 # pragma: no cover
self = MockedSelf() # pragma: no cover
check_ops = MockedCheckOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
