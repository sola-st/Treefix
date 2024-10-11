import unittest # pragma: no cover
import re # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda obj: (obj if hasattr(obj, '__iter__') else (_ for _ in ()).throw(TypeError("to be iterable")))})() # pragma: no cover

import unittest # pragma: no cover

class CheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(obj): # pragma: no cover
        if not hasattr(obj, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockSelf(unittest.TestCase): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
check_ops = CheckOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
