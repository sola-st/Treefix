import numpy as np # pragma: no cover
import unittest # pragma: no cover

unit = 'BYTE' # pragma: no cover
pos = 5 # pragma: no cover
dtype = np.int32 # pragma: no cover
class Mock(unittest.TestCase): # pragma: no cover
    def cached_session(self): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): return self # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): pass # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ExceptionContextManager: # pragma: no cover
            def __enter__(self): pass # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f'{exception.__name__} not raised') # pragma: no cover
        return ExceptionContextManager() # pragma: no cover
    def evaluate(self, op): raise errors_impl.InvalidArgumentError(None, None, 'Invalid slice index') # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Scalar/Scalar
from l3.Runtime import _l_
test_string = {
    "BYTE": b"Hello",
    "UTF8_CHAR": u"H\xc3ll\U0001f604".encode("utf-8"),
}[unit]
_l_(22188)
position = np.array(pos, dtype)
_l_(22189)
length = np.array(3, dtype)
_l_(22190)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
_l_(22191)
with self.cached_session():
    _l_(22194)

    with self.assertRaises(errors_impl.InvalidArgumentError):
        _l_(22193)

        self.evaluate(substr_op)
        _l_(22192)
