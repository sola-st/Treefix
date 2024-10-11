import numpy as np # pragma: no cover

import numpy as np # pragma: no cover

self = type('MockSelf', (object,), {'cached_session': lambda: contextlib.nullcontext(), 'assertRaises': lambda exc_type: (lambda func: None), 'evaluate': lambda x: x})() # pragma: no cover
errors_impl = type('MockErrorsImpl', (object,), {'InvalidArgumentError': Exception})() # pragma: no cover

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
