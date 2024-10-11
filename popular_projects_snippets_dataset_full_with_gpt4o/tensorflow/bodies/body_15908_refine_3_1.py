DynamicRaggedShape = type('Mock', (object,), {'_from_inner_shape': lambda x: ragged_tensor.RaggedTensor.from_row_splits(x, [0, len(x)])}) # pragma: no cover

class MockTestCase:# pragma: no cover
    def assertRaisesRegex(self, exception, regex):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                pass# pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
                if not exc_type or not issubclass(exc_type, exception):# pragma: no cover
                    raise AssertionError(f'Expected {exception} but got {exc_type}')# pragma: no cover
                if not regex in str(exc_val):# pragma: no cover
                    raise AssertionError(f'Expected exception message to contain {regex} but got {exc_val}')# pragma: no cover
                return True# pragma: no cover
        return ContextManager()# pragma: no cover
self = MockTestCase() # pragma: no cover
class DynamicRaggedShape:# pragma: no cover
    @staticmethod# pragma: no cover
    def _from_inner_shape(tensor):# pragma: no cover
        return ragged_tensor.RaggedTensor.from_tensor(tensor)# pragma: no cover
    def _as_row_partitions(self):# pragma: no cover
        pass # pragma: no cover

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
