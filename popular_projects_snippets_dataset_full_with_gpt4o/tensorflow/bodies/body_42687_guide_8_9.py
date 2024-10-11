class MockSelf: # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaises(exception): # pragma: no cover
        class Expector(contextlib.AbstractContextManager): # pragma: no cover
            def __init__(self, exc): # pragma: no cover
                self.exc = exc # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not issubclass(exc_type, self.exc): # pragma: no cover
                    raise AssertionError(f'{self.exc} not raised') # pragma: no cover
        return Expector(exception) # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaisesRegex(exception, regex): # pragma: no cover
        class Expector(contextlib.AbstractContextManager): # pragma: no cover
            def __init__(self, exc): # pragma: no cover
                self.exc = exc # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not issubclass(exc_type, self.exc): # pragma: no cover
                    raise AssertionError(f'{self.exc} not raised') # pragma: no cover
        return Expector(exception) # pragma: no cover
self = MockSelf() # pragma: no cover

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
