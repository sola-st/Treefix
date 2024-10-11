self = type('MockSelf', (object,), {'assertRaises': lambda *args, **kwargs: None, 'assertRaisesRegex': lambda *args, **kwargs: None})() # pragma: no cover

self = type('MockSelf', (object,), {'assertRaises': lambda *args: type('MockContextManager', (object,), {'__enter__': lambda s: None, '__exit__': lambda s, exc_type, exc_value, traceback: exc_type is not None and issubclass(exc_type, args[0])}), 'assertRaisesRegex': lambda *args: type('MockContextManager', (object,), {'__enter__': lambda s: None, '__exit__': lambda s, exc_type, exc_value, traceback: exc_type is not None and issubclass(exc_type, args[0]) and (not args[1] or re.search(args[1], str(exc_value)) is not None)})})() # pragma: no cover
core = type('MockCore', (object,), {'_FallbackException': type('MockFallbackException', (BaseException,), {})})() # pragma: no cover

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
