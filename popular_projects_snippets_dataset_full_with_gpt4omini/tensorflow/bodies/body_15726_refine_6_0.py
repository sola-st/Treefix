class Mock: pass # pragma: no cover
RaggedTensor = type('RaggedTensor', (object,), { 'from_uniform_row_length': staticmethod(lambda x, y: tf.ragged.constant(x, ragged_rank=1)), 'from_row_splits': staticmethod(lambda values, splits: tf.ragged.constant(values, splits=splits)) }) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = [[1, 2, 3], [4, 5]] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 3, 5] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover
class TestClass: pass # pragma: no cover
self = TestClass() # pragma: no cover
slice_spec = slice(0, None, None) # pragma: no cover
expected_shape = (1, 3) # pragma: no cover

class RaggedTensor: # pragma: no cover
    @staticmethod# pragma: no cover
    def from_uniform_row_length(values, row_length):# pragma: no cover
        return tf.ragged.constant(values)# pragma: no cover
# pragma: no cover
    @staticmethod# pragma: no cover
    def from_row_splits(values, splits):# pragma: no cover
        pass
EXAMPLE_RAGGED_TENSOR_3D_VALUES = [[1, 2, 3], [4, 5], [6]] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 3, 5, 6] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover
class MockSelf: # pragma: no cover
    def assertAllEqual(self, a, b): assert tf.reduce_all(tf.equal(a, b)).numpy() # pragma: no cover
    def assertIsNot(self, a, b): assert a is not b # pragma: no cover
    def _TestGetItem(self, rt, slice_spec, expected, expected_shape): # pragma: no cover
        actual = rt.__getitem__(slice_spec)# pragma: no cover
        assert tf.reduce_all(tf.equal(actual, expected)).numpy() # pragma: no cover
self = MockSelf() # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D = RaggedTensor.from_row_splits(EXAMPLE_RAGGED_TENSOR_3D_VALUES, EXAMPLE_RAGGED_TENSOR_3D_SPLITS) # pragma: no cover
slice_spec = slice(0, 2) # pragma: no cover

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
