import unittest # pragma: no cover

check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda x: (_ for _ in ()).throw(TypeError('to be iterable'))})() # pragma: no cover
self = type('MockTestCase', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover

import unittest # pragma: no cover

class CheckOpsMock: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(val): # pragma: no cover
        if not hasattr(val, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
check_ops = CheckOpsMock() # pragma: no cover
self = type('MockTest', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
