import unittest # pragma: no cover
import re # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda obj: (obj if hasattr(obj, '__iter__') else (_ for _ in ()).throw(TypeError("to be iterable")))})() # pragma: no cover

import unittest # pragma: no cover

class TestCaseWithRaiseRegex(unittest.TestCase): # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs): # pragma: no cover
        with unittest.TestCase().assertRaisesRegexp(expected_exception, expected_regex): # pragma: no cover
            return super().assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs) # pragma: no cover
 # pragma: no cover
self = TestCaseWithRaiseRegex() # pragma: no cover
 # pragma: no cover
def mock_assert_proper_iterable(it): # pragma: no cover
    if not hasattr(it, '__iter__'): # pragma: no cover
        raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockCheckOps: # pragma: no cover
    assert_proper_iterable = staticmethod(mock_assert_proper_iterable) # pragma: no cover
 # pragma: no cover
check_ops = MockCheckOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
