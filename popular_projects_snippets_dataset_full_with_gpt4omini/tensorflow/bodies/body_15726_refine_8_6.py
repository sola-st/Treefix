class Mock: pass # pragma: no cover
RaggedTensor = type('MockRaggedTensor', (object,), { 'from_uniform_row_length': staticmethod(lambda x: x), 'from_row_splits': staticmethod(lambda values, splits: ragged.constant(values, ragged_splits=splits)) }) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 3, 6, 9] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover

class MockRaggedTensor:  # pragma: no cover
    @staticmethod # pragma: no cover
    def from_uniform_row_length(values, row_length): # pragma: no cover
        return tf.ragged.constant(values) # pragma: no cover
    @staticmethod # pragma: no cover
    def from_row_splits(values, splits): # pragma: no cover
        pass
RaggedTensor = MockRaggedTensor # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = [[1, 2, 3], [4, 5], [6]] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 3, 5, 6] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'assertAllEqual': lambda self, a, b: print('Assert All Equal:', a == b), # pragma: no cover
    'assertIsNot': lambda self, a, b: print('Assert Is Not:', a is not b), # pragma: no cover
    '_TestGetItem': lambda self, rt, slice_spec, expected, expected_shape: None # pragma: no cover
})() # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D = RaggedTensor.from_row_splits(EXAMPLE_RAGGED_TENSOR_3D_VALUES, EXAMPLE_RAGGED_TENSOR_3D_SPLITS) # pragma: no cover
slice_spec = slice(0, 2) # pragma: no cover
expected_shape = (2, 3) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
from l3.Runtime import _l_
"""Test that rt.__getitem__(slice_spec) == expected."""
rt = RaggedTensor.from_uniform_row_length(
    RaggedTensor.from_row_splits(EXAMPLE_RAGGED_TENSOR_3D_VALUES,
                                 EXAMPLE_RAGGED_TENSOR_3D_SPLITS),
    EXAMPLE_RAGGED_TENSOR_3D_ROWLEN)
_l_(6072)
self.assertAllEqual(rt, EXAMPLE_RAGGED_TENSOR_3D)
_l_(6073)
self.assertIsNot(rt.uniform_row_length, None)
_l_(6074)
self._TestGetItem(rt, slice_spec, expected, expected_shape)
_l_(6075)

# If the result is 3D, then check that it still has a uniform row length:
actual = rt.__getitem__(slice_spec)  # pylint: disable=assignment-from-no-return
_l_(6076)  # pylint: disable=assignment-from-no-return
if actual.shape.rank == 3:
    _l_(6079)

    self.assertIsNot(actual.uniform_row_length, None)
    _l_(6077)
    self.assertAllEqual(actual.uniform_row_length, expected_shape[1])
    _l_(6078)
