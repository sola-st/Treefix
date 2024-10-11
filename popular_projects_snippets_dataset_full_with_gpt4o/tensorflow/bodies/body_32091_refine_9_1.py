import numpy as np # pragma: no cover

unit = 'UTF8_CHAR' # pragma: no cover
pos = [1] # pragma: no cover
dtype = np.int32 # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda x: None, 'assertRaises': lambda x, y: None})() # pragma: no cover
self.cached_session = lambda: type('MockSession', (object,), {'__enter__': lambda x: None, '__exit__': lambda x, y, z, w: None})(self) # pragma: no cover
self.assertRaises = lambda exc: type('ContextManager', (object,), {'__enter__': lambda x: None, '__exit__': lambda x, y, z, w: None})() # pragma: no cover
self.evaluate = lambda x: None # pragma: no cover

import numpy as np # pragma: no cover

unit = 'BYTE' # pragma: no cover
pos = [1] # pragma: no cover
dtype = np.int32 # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda self: type('MockSession', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, exc_type, exc_val, exc_tb: None})(), 'assertRaises': lambda self, exc: type('MockAssertRaises', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, exc_type, exc_val, exc_tb: None}), 'evaluate': lambda self, op: op})() # pragma: no cover

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
