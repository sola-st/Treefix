import unittest # pragma: no cover

class CheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__') and not isinstance(value, str): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
check_ops = CheckOps() # pragma: no cover
class MockSelf(unittest.TestCase): # pragma: no cover
    def runTest(self): pass # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
