class DynamicRaggedShape: # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(x): # pragma: no cover
        raise ValueError('Expected error for testing') # pragma: no cover
    def _as_row_partitions(self): # pragma: no cover
        pass # pragma: no cover
class TestClass: # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaisesRegex(exception, regex): # pragma: no cover
        class Context: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not exc_value: # pragma: no cover
                    raise AssertionError('Exception not raised') # pragma: no cover
                if not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f'Different exception raised: expected {exception}, got {exc_type}') # pragma: no cover
                if regex not in str(exc_value): # pragma: no cover
                    raise AssertionError(f'Exception message does not match regex: {regex}') # pragma: no cover
                return True # pragma: no cover
        return Context() # pragma: no cover
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
