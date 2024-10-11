class MockSelf:# pragma: no cover
    def assertRaisesRegex(self, exception, pattern):# pragma: no cover
        # Mock implementation# pragma: no cover
        pass# pragma: no cover
self = MockSelf() # pragma: no cover
class MockFunction:# pragma: no cover
    @staticmethod# pragma: no cover
    def function(input_signature):# pragma: no cover
        return lambda f: f# pragma: no cover
# pragma: no cover
def_function = MockFunction() # pragma: no cover
class MockTensorSpec:# pragma: no cover
    def __init__(self, shape, dtype):# pragma: no cover
        self.shape = shape# pragma: no cover
        self.dtype = dtype# pragma: no cover
    @staticmethod# pragma: no cover
    def TensorSpec(shape, dtype):# pragma: no cover
        return MockTensorSpec(shape, dtype)# pragma: no cover
tensor_spec = MockTensorSpec # pragma: no cover
class MockDtypes:# pragma: no cover
    int32 = 'int32'# pragma: no cover
dtypes = MockDtypes() # pragma: no cover
class MockDynamicRaggedShape:# pragma: no cover
    @staticmethod# pragma: no cover
    def _from_inner_shape(x):# pragma: no cover
        return x# pragma: no cover
    def _as_row_partitions(self):# pragma: no cover
        pass# pragma: no cover
DynamicRaggedShape = MockDynamicRaggedShape # pragma: no cover

class MockContextManager:# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        pass# pragma: no cover
class MockSelf:# pragma: no cover
    def assertRaisesRegex(self, exception, pattern):# pragma: no cover
        return MockContextManager()# pragma: no cover
self = MockSelf() # pragma: no cover
class MockFunction:# pragma: no cover
    @staticmethod# pragma: no cover
    def function(input_signature):# pragma: no cover
        return lambda f: f# pragma: no cover
# pragma: no cover
def_function = MockFunction() # pragma: no cover
class MockTensorSpec:# pragma: no cover
    def __init__(self, shape, dtype):# pragma: no cover
        self.shape = shape# pragma: no cover
        self.dtype = dtype# pragma: no cover
    @staticmethod# pragma: no cover
    def TensorSpec(shape, dtype):# pragma: no cover
        return MockTensorSpec(shape, dtype)# pragma: no cover
tensor_spec = MockTensorSpec # pragma: no cover
class MockDtypes:# pragma: no cover
    int32 = 'int32'# pragma: no cover
dtypes = MockDtypes() # pragma: no cover
class MockDynamicRaggedShape:# pragma: no cover
    @staticmethod# pragma: no cover
    def _from_inner_shape(x):# pragma: no cover
        return x# pragma: no cover
    def _as_row_partitions(self):# pragma: no cover
        pass# pragma: no cover
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
