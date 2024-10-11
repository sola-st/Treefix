import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
RaggedTensor = type('RaggedTensor', (object,), { # pragma: no cover
    'from_uniform_row_length': lambda values, row_length: tf.ragged.constant(values, row_splits=[0, row_length]), # pragma: no cover
    'from_row_splits': lambda values, splits: tf.ragged.constant(values, row_splits=splits), # pragma: no cover
}) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.int32) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = np.array([0, 2, 2], dtype=np.int32) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 2 # pragma: no cover
self = Mock() # pragma: no cover
self.assertAllEqual = lambda a, b: tf.assert_equal(a, b) # pragma: no cover

import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
RaggedTensor = type('RaggedTensor', (object,), { # pragma: no cover
    'from_uniform_row_length': staticmethod(lambda values, row_length: tf.ragged.constant(values, ragged_rank=1)), # pragma: no cover
    'from_row_splits': staticmethod(lambda values, splits: tf.ragged.constant(values, row_splits=splits)), # pragma: no cover
}) # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_VALUES = [[[1, 2], [3]], [[4, 5, 6], [7, 8]]] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 2, 2, 3] # pragma: no cover
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
