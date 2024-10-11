self = type('MockSelf', (), {'assertRaisesRegex': lambda *args: (args[-1](),)})() # pragma: no cover
def_function = type('MockDefFunction', (), {'function': lambda self, input_signature: lambda f: f})() # pragma: no cover
tensor_spec = type('MockTensorSpec', (object,), {'TensorSpec': staticmethod(lambda shape, dtype: (shape, dtype))}) # pragma: no cover
dtypes = type('MockDTypes', (), {'int32': 'int32'})() # pragma: no cover
DynamicRaggedShape = type('MockDynamicRaggedShape', (), {'_from_inner_shape': staticmethod(lambda x: type('MockRaggedShape', (), {'_as_row_partitions': lambda self: None})())})() # pragma: no cover

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
