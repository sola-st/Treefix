import unittest # pragma: no cover

self = type('Mock', (object,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover

DynamicRaggedShape = type('Mock', (object,), {'_from_inner_shape': lambda x: ragged_tensor.RaggedTensor.from_row_lengths(x, [len(x)])}) # pragma: no cover

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
