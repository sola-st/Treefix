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
        if not hasattr(it, '__iter__'): # pragma: no cover
            raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
class MockedSelf: # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaisesRegex(exc_type, regex, *args, **kwargs): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): return self # pragma: no cover
            def __exit__(self, exc_type_internal, exc_value, traceback): # pragma: no cover
                if not exc_type_internal: raise AssertionError('TypeError not raised') # pragma: no cover
                if not issubclass(exc_type_internal, exc_type): raise AssertionError('Mismatched exception type') # pragma: no cover
                if not re.search(regex, str(exc_value)): raise AssertionError('Regex mismatch') # pragma: no cover
        return ContextManager() # pragma: no cover
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
