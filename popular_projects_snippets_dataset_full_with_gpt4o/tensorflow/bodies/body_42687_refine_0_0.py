class MockSelf: # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f"Expected {exception}, but got {exc_type}") # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
    def assertRaisesRegex(self, exception, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f"Expected {exception}, but got {exc_type}") # pragma: no cover
                if not re.search(regex, str(exc_val)): # pragma: no cover
                    raise AssertionError(f"Expected error message to match {regex}, but got {exc_val}") # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

 # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f"Expected {exception}, but got {exc_type}") # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
    def assertRaisesRegex(self, exception, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f"Expected {exception}, but got {exc_type}") # pragma: no cover
                if not re.search(regex, str(exc_val)): # pragma: no cover
                    raise AssertionError(f"Expected error message to match {regex}, but got {exc_val}") # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
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
