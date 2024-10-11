import unittest # pragma: no cover

class DynamicRaggedShape: # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(x): # pragma: no cover
        return DynamicRaggedShape() # pragma: no cover
 # pragma: no cover
    def _as_row_partitions(self): # pragma: no cover
        raise ValueError('Test error message for assertRaisesRegex validation') # pragma: no cover
 # pragma: no cover
class MockTestCase(unittest.TestCase): # pragma: no cover
    def runTest(self): # pragma: no cover
        pass # pragma: no cover
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
