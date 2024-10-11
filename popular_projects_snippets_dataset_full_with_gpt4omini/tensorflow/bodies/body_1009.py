# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/segment_reduction_ops_test.py
for dtype in self.numeric_types:
    self.assertAllClose(
        np.array([0, 1, 2], dtype=dtype),
        self._segmentProdV2(
            np.array([0, 1, 2, 3, 4, 5], dtype=dtype),
            np.array([0, 0, 2, 3, 3, 3], dtype=np.int32), 3))
