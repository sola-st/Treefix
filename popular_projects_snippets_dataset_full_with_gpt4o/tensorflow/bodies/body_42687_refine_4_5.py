self = type('MockSelf', (object,), {'assertRaises': lambda *args, **kwargs: None, 'assertRaisesRegex': lambda *args, **kwargs: None})() # pragma: no cover

import re # pragma: no cover

self = type('MockSelf', (object,), {'assertRaises': lambda self, exc: contextlib.nullcontext(), 'assertRaisesRegex': lambda self, exc, reg: contextlib.nullcontext()})() # pragma: no cover
core = type('MockCore', (object,), {'_FallbackException': type('MockFallbackException', (Exception,), {})})() # pragma: no cover
pywrap_tfe = type('MockPywrapTFE', (object,), {'TFE_Py_FastPathExecute': lambda *args, **kwargs: None, 'TFE_Py_Execute': lambda *args, **kwargs: None})() # pragma: no cover

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
