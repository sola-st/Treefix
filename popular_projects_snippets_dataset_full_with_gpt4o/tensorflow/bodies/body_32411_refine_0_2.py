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

import unittest # pragma: no cover

class MockedCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(it): # pragma: no cover
        if not isinstance(it, (list, tuple, set, dict)) and not hasattr(it, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockedSelf: # pragma: no cover
    def assertRaisesRegex(self, exc_type, regex, *args, **kwargs): # pragma: no cover
        class _ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type_inner, exc_value, traceback): # pragma: no cover
                if exc_type_inner is None: # pragma: no cover
                    raise AssertionError(f'{exc_type.__name__} not raised') # pragma: no cover
                if not re.search(regex, str(exc_value)) or not issubclass(exc_type_inner, exc_type): # pragma: no cover
                    raise AssertionError(f'Expected {exc_type.__name__} with message matching {regex}, got {exc_value}') # pragma: no cover
                return True # pragma: no cover
        return _ContextManager() # pragma: no cover
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
