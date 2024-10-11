import unittest # pragma: no cover

self = unittest.TestCase() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda x: (x if hasattr(x, '__iter__') else (_ for _ in ()).throw(TypeError('Non-iterables are not allowed')))})() # pragma: no cover

import unittest # pragma: no cover
import re # pragma: no cover

class MockCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex, callable_obj=None, *args, **kwargs): # pragma: no cover
        if callable_obj is None: # pragma: no cover
            raise ValueError('callable_obj must be provided') # pragma: no cover
        try: # pragma: no cover
            callable_obj() # pragma: no cover
        except expected_exception as e: # pragma: no cover
            if not re.search(expected_regex, str(e)): # pragma: no cover
                raise AssertionError(f'"{expected_regex}" does not match "{str(e)}"') # pragma: no cover
        else: # pragma: no cover
            raise AssertionError(f'{expected_exception.__name__} not raised') # pragma: no cover
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
