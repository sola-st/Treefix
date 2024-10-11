class DynamicRaggedShapeMock: # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(x): # pragma: no cover
        raise ValueError('Mocked Error') # pragma: no cover
 # pragma: no cover
    def _as_row_partitions(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockTestCase: # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaisesRegex(exc, pattern): # pragma: no cover
        class Manager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
 # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not exc_value: # pragma: no cover
                    raise AssertionError('Exception not raised') # pragma: no cover
                if not isinstance(exc_value, exc): # pragma: no cover
                    raise AssertionError('Different exception raised') # pragma: no cover
                if not pattern in str(exc_value): # pragma: no cover
                    raise AssertionError('Pattern not in exception string') # pragma: no cover
                return True # pragma: no cover
        return Manager() # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover

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
