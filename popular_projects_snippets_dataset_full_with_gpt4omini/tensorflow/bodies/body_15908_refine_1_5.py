self = type('Mock', (), {'assertRaisesRegex': staticmethod(lambda *args: None)})() # pragma: no cover
DynamicRaggedShape = type('Mock', (), {'_from_inner_shape': staticmethod(lambda x: type('Mock', (), {'_as_row_partitions': lambda self: None})())}) # pragma: no cover

class MockSelf:  # Mock for 'self' # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaisesRegex(exc_type, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                return False # pragma: no cover
        return ContextManager() # pragma: no cover
self = MockSelf() # pragma: no cover
def_function = type('MockFunction', (), {'function': lambda input_signature: lambda f: f})() # pragma: no cover
class MockDynamicRaggedShape: # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(x): # pragma: no cover
        class MockRaggedShape: # pragma: no cover
            def _as_row_partitions(self): # pragma: no cover
                pass # pragma: no cover
        return MockRaggedShape() # pragma: no cover
DynamicRaggedShape = MockDynamicRaggedShape # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Error is readable, but does not match strings correctly.
from l3.Runtime import _l_
with self.assertRaisesRegex(ValueError, ''):
    _l_(7697)


    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        _l_(7695)

        rts = DynamicRaggedShape._from_inner_shape(x)
        _l_(7693)
        rts._as_row_partitions()
        _l_(7694)

    foo([3, 7, 5])
    _l_(7696)
