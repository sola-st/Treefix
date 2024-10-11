# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
self._assertForwardOpMatchesExpected(
    np.array([[1, 2], [3, 4]], dtype=np.float32), [4, 4],
    expected=np.array(
        [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]],
        dtype=np.float32),
    large_tolerance=True)
