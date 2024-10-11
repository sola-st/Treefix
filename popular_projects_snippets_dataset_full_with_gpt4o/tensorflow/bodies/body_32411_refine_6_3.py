import unittest # pragma: no cover
import re # pragma: no cover

class MockCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__'): # pragma: no cover
            raise TypeError('Expected an object to be iterable') # pragma: no cover
 # pragma: no cover
check_ops = MockCheckOps() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs): # pragma: no cover
        if len(args) == 0: # pragma: no cover
            raise ValueError('assertRaisesRegex needs a callable as an argument') # pragma: no cover
        callable_obj = args[0] # pragma: no cover
        try: # pragma: no cover
            callable_obj() # pragma: no cover
        except expected_exception as e: # pragma: no cover
            if re.search(expected_regex, str(e)) is None: # pragma: no cover
                raise AssertionError(f'Exception message does not match: {e}') # pragma: no cover
        else: # pragma: no cover
            raise AssertionError('Expected exception was not raised') # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

import unittest # pragma: no cover

class MockCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
check_ops = MockCheckOps() # pragma: no cover
 # pragma: no cover
class MockSelf(unittest.TestCase): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
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
