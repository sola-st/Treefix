import numpy as np # pragma: no cover

unit = 'BYTE' # pragma: no cover
pos = 1 # pragma: no cover
dtype = np.int32 # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda s: type('MockSession', (object,), {'__enter__': lambda ses: None, '__exit__': lambda ses, exc_type, exc_value, traceback: None})(), 'assertRaises': lambda s, exc_type: type('MockAssertRaises', (object,), {'__enter__': lambda ar: None, '__exit__': lambda ar, exc_type, exc_value, traceback: None})()})() # pragma: no cover
self.evaluate = lambda x: None # pragma: no cover

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
