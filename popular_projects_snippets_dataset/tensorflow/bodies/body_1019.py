# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
"""Tests for min, max, and prod ops.

    These share most of their implementation with sum, so we only test basic
    functionality.
    """
for dtype in self.numeric_types:
    self.assertAllClose(
        np.array([8, 3, 1, 0], dtype=dtype),
        self._unsortedSegmentProd(
            np.array([0, 1, 2, 3, 4, 5, 6], dtype=dtype),
            np.array([3, -1, 0, 1, 0, -1, 3], dtype=np.int32), 4))

for dtype in self.int_types | self.float_types:
    minval = dtypes.as_dtype(dtype).min
    maxval = dtypes.as_dtype(dtype).max

    self.assertAllClose(
        np.array([2, 3, maxval, 0], dtype=dtype),
        self._unsortedSegmentMin(
            np.array([0, 1, 2, 3, 4, 5, 6], dtype=dtype),
            np.array([3, -1, 0, 1, 0, -1, 3], dtype=np.int32), 4))
    self.assertAllClose(
        np.array([4, 3, minval, 6], dtype=dtype),
        self._unsortedSegmentMax(
            np.array([0, 1, 2, 3, 4, 5, 6], dtype=dtype),
            np.array([3, -1, 0, 1, 0, -1, 3], dtype=np.int32), 4))
