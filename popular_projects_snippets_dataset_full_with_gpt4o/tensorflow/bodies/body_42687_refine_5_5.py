import unittest # pragma: no cover

self = type('Mock', (object,), {'assertRaises': unittest.TestCase().assertRaises, 'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover

import unittest.mock as mock # pragma: no cover
import re # pragma: no cover

self = type('MockSelf', (object,), { # pragma: no cover
    'assertRaises': lambda self, exc: mock.MagicMock(__enter__=lambda s: s, __exit__=lambda s, exc_type, exc_val, exc_tb: issubclass(exc_type, exc)), # pragma: no cover
    'assertRaisesRegex': lambda self, exc, regex: mock.MagicMock(__enter__=lambda s: s, __exit__=lambda s, exc_type, exc_val, exc_tb: issubclass(exc_type, exc) and re.search(regex, str(exc_val)) is not None) # pragma: no cover
})() # pragma: no cover
core = type('MockCore', (object,), {'_FallbackException': type('MockFallbackException', (Exception,), {})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
from l3.Runtime import _l_
split_dim = constant_op.constant(0, dtype=dtypes.int32)
_l_(15618)
value = [0, 1, 2, 3]
_l_(15619)
ctx = context.context()
_l_(15620)
ctx.ensure_initialized()
_l_(15621)

with self.assertRaises(core._FallbackException):
    _l_(15623)

    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "Split", None, split_dim, value,
                                      "num_split", 1000000000000)
    _l_(15622)

value = constant_op.constant(value)
_l_(15624)
attrs = ("num_split", 1000000000000, "T", value.dtype.as_datatype_enum)
_l_(15625)
with self.assertRaisesRegex(ValueError, "Number of outputs is too big"):
    _l_(15627)

    pywrap_tfe.TFE_Py_Execute(ctx._handle, None, "Split", [split_dim, value],
                              attrs, 1000000000000)
    _l_(15626)
