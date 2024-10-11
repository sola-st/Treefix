# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
self._assertForwardOpMatchesExpected(
    np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        dtype=np.float32), [3, 3],
    expected=np.array([[1, 3, 4], [9, 11, 12], [13, 15, 16]],
                      dtype=np.float32))
