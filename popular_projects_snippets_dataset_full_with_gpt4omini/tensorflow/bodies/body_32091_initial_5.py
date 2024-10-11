import numpy as np # pragma: no cover

unit = 'BYTE' # pragma: no cover
pos = [0] # pragma: no cover
dtype = np.uint8 # pragma: no cover
string_ops = type('MockStringOps', (object,), {'substr': lambda test_string, position, length, unit: test_string[unit][position[0]:position[0]+length]}) # pragma: no cover
self = type('Mock', (), {'cached_session': lambda: type('MockSession', (), {'__enter__': lambda s: None, '__exit__': lambda s, exc_type, exc_value, traceback: None}), 'assertRaises': lambda self, exc: (lambda: None), 'evaluate': lambda x: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Scalar/Scalar
from l3.Runtime import _l_
test_string = {
    "BYTE": b"Hello",
    "UTF8_CHAR": u"H\xc3ll\U0001f604".encode("utf-8"),
}[unit]
_l_(9933)
position = np.array(pos, dtype)
_l_(9934)
length = np.array(3, dtype)
_l_(9935)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
_l_(9936)
with self.cached_session():
    _l_(9939)

    with self.assertRaises(errors_impl.InvalidArgumentError):
        _l_(9938)

        self.evaluate(substr_op)
        _l_(9937)
