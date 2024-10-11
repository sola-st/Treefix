self = type('Mock', (object,), {'assertRaises': lambda self, exc: None, 'assertRaisesRegex': lambda self, exc, msg: None})() # pragma: no cover
pywrap_tfe = type('Mock', (object,), {'TFE_Py_FastPathExecute': lambda *args: None, 'TFE_Py_Execute': lambda *args: None})() # pragma: no cover

self = type('Mock', (object,), {'assertRaises': lambda self, exc: None, 'assertRaisesRegex': lambda self, exc, msg: None})() # pragma: no cover
core = type('Mock', (object,), {'_FallbackException': Exception})() # pragma: no cover
pywrap_tfe = type('Mock', (object,), {'TFE_Py_FastPathExecute': lambda ctx, op, *args: None, 'TFE_Py_Execute': lambda ctx, op, inputs, attrs, num_split: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
from l3.Runtime import _l_
split_dim = constant_op.constant(0, dtype=dtypes.int32)
_l_(4328)
value = [0, 1, 2, 3]
_l_(4329)
ctx = context.context()
_l_(4330)
ctx.ensure_initialized()
_l_(4331)

with self.assertRaises(core._FallbackException):
    _l_(4333)

    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "Split", None, split_dim, value,
                                      "num_split", 1000000000000)
    _l_(4332)

value = constant_op.constant(value)
_l_(4334)
attrs = ("num_split", 1000000000000, "T", value.dtype.as_datatype_enum)
_l_(4335)
with self.assertRaisesRegex(ValueError, "Number of outputs is too big"):
    _l_(4337)

    pywrap_tfe.TFE_Py_Execute(ctx._handle, None, "Split", [split_dim, value],
                              attrs, 1000000000000)
    _l_(4336)
