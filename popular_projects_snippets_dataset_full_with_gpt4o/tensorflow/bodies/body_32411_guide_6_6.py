import unittest # pragma: no cover

class CheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__'): raise TypeError('to be iterable') # pragma: no cover
check_ops = CheckOps() # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaisesRegex(self, exc_class, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self_): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self_, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not re.match(regex, str(exc_value)): # pragma: no cover
                    raise AssertionError(f'{exc_class.__name__} matched {regex} not raised') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
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
