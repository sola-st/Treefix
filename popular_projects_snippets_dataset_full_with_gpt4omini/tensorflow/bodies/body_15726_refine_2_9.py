EXAMPLE_RAGGED_TENSOR_3D_VALUES = [[1, 2, 3], [4, 5], [6]] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 3, 5, 6] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover
self = type('MockSelf', (), { 'assertAllEqual': lambda self, x, y: None, 'assertIsNot': lambda self, x, y: None, '_TestGetItem': lambda self, rt, slice_spec, expected, expected_shape: None })() # pragma: no cover
slice_spec = slice(None) # pragma: no cover
expected_shape = (3, 3, 1) # pragma: no cover

class Mock: pass # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = [[1, 2, 3], [4, 5], [6]] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 3, 5, 6] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover
self = Mock() # pragma: no cover

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
