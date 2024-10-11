import unittest # pragma: no cover

self = type('MockSelf', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover
check_ops = type('MockCheckOps', (object,), {'assert_proper_iterable': lambda x: (iter(x) or True) if isinstance(x, (list, tuple, set, dict, str, bytes)) else (_ for _ in ()).throw(TypeError('to be iterable'))})() # pragma: no cover

import unittest # pragma: no cover

class MockedCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(it): # pragma: no cover
        if not hasattr(it, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockedSelf(unittest.TestCase): # pragma: no cover
    def runTest(self): # pragma: no cover
        pass # pragma: no cover
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
