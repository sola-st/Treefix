import numpy as np # pragma: no cover

class RaggedTensor: # pragma: no cover
    @staticmethod # pragma: no cover
    def from_row_splits(values, splits): # pragma: no cover
        return rt.RaggedTensor.from_row_splits(values, splits) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def from_uniform_row_length(ragged_tensor, uniform_row_length): # pragma: no cover
        return rt.RaggedTensor.from_uniform_row_length(ragged_tensor, uniform_row_length) # pragma: no cover
 # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 1, 3] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 2 # pragma: no cover
slice_spec = slice(0, 2) # pragma: no cover
expected_shape = (2, 2, 3) # pragma: no cover
 # pragma: no cover
class TestClass: # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        assert np.array_equal(a, b), f'{a} is not equal to {b}' # pragma: no cover
 # pragma: no cover
    def assertIsNot(self, a, b): # pragma: no cover
        assert a is not b, f'{a} is {b}' # pragma: no cover
 # pragma: no cover
    def _TestGetItem(self, rt, slice_spec, expected, expected_shape): # pragma: no cover
        actual = rt.__getitem__(slice_spec) # pragma: no cover
        self.assertAllEqual(actual, expected) # pragma: no cover
        self.assertAllEqual(actual.shape, expected_shape) # pragma: no cover
 # pragma: no cover
test_instance = TestClass() # pragma: no cover
self = test_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
from l3.Runtime import _l_
"""Test that rt.__getitem__(slice_spec) == expected."""
rt = RaggedTensor.from_uniform_row_length(
    RaggedTensor.from_row_splits(EXAMPLE_RAGGED_TENSOR_3D_VALUES,
                                 EXAMPLE_RAGGED_TENSOR_3D_SPLITS),
    EXAMPLE_RAGGED_TENSOR_3D_ROWLEN)
_l_(18113)
self.assertAllEqual(rt, EXAMPLE_RAGGED_TENSOR_3D)
_l_(18114)
self.assertIsNot(rt.uniform_row_length, None)
_l_(18115)
self._TestGetItem(rt, slice_spec, expected, expected_shape)
_l_(18116)

# If the result is 3D, then check that it still has a uniform row length:
actual = rt.__getitem__(slice_spec)  # pylint: disable=assignment-from-no-return
_l_(18117)  # pylint: disable=assignment-from-no-return
if actual.shape.rank == 3:
    _l_(18120)

    self.assertIsNot(actual.uniform_row_length, None)
    _l_(18118)
    self.assertAllEqual(actual.uniform_row_length, expected_shape[1])
    _l_(18119)
