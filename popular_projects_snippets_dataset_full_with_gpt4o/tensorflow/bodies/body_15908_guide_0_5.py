class DynamicRaggedShape: # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(x): # pragma: no cover
        if not isinstance(x, list) or not all(isinstance(i, int) for i in x): # pragma: no cover
            raise ValueError('Input must be a list of integers') # pragma: no cover
        return DynamicRaggedShape() # pragma: no cover
 # pragma: no cover
    def _as_row_partitions(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class TestClass: # pragma: no cover
    def assertRaisesRegex(self, exception, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is not exception: # pragma: no cover
                    raise AssertionError(f'Expected {exception}, but got {exc_type}') # pragma: no cover
                if not exc_value or not isinstance(exc_value, exception): # pragma: no cover
                    raise AssertionError(f'Exception does not match: {exc_value}') # pragma: no cover
                if regex not in str(exc_value): # pragma: no cover
                    raise AssertionError(f'Error message does not match regex: {regex}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
self = TestClass() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Error is readable, but does not match strings correctly.
from l3.Runtime import _l_
with self.assertRaisesRegex(ValueError, ''):
    _l_(20748)


    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        _l_(20746)

        rts = DynamicRaggedShape._from_inner_shape(x)
        _l_(20744)
        rts._as_row_partitions()
        _l_(20745)

    foo([3, 7, 5])
    _l_(20747)
