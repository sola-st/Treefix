import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda x: (x if hasattr(x, '__iter__') else (_ for _ in ()).throw(TypeError('to be iterable')) )})() # pragma: no cover

import unittest # pragma: no cover
import re # pragma: no cover

class MockCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __init__(self, expected_exception, expected_regex): # pragma: no cover
                self.expected_exception = expected_exception # pragma: no cover
                self.expected_regex = expected_regex # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type: # pragma: no cover
                    raise AssertionError(f'{self.expected_exception.__name__} not raised') # pragma: no cover
                if not re.search(self.expected_regex, str(exc_value)): # pragma: no cover
                    raise AssertionError(f'{exc_value} does not match {self.expected_regex}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager(expected_exception, expected_regex) # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
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
