import numpy as np # pragma: no cover

EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 3 # pragma: no cover
slice_spec = slice(0, 2) # pragma: no cover
expected_shape = np.array([2, 3]) # pragma: no cover

import numpy as np # pragma: no cover

EXAMPLE_RAGGED_TENSOR_3D_VALUES = [10, 20, 30, 40, 50, 60] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_SPLITS = [0, 2, 3, 6] # pragma: no cover
EXAMPLE_RAGGED_TENSOR_3D_ROWLEN = 2 # pragma: no cover
slice_spec = slice(0, 2) # pragma: no cover
expected_shape = [2, 2] # pragma: no cover

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
