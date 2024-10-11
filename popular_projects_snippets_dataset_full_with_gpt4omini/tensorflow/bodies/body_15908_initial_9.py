class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
class DynamicRaggedShape:# pragma: no cover
    @staticmethod# pragma: no cover
    def _from_inner_shape(x):# pragma: no cover
        return ragged_tensor.RaggedTensor.from_row_splits(x, [0] + list(x))# pragma: no cover
    def _as_row_partitions(self): pass# pragma: no cover
DynamicRaggedShape = DynamicRaggedShape # pragma: no cover

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
