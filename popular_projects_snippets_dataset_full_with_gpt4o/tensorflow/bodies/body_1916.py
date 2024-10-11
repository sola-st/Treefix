# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
self._assertForwardOpMatchesExpected(
    np.array([[1, 2], [3, 4]], dtype=np.float32), [3, 3],
    expected=np.array([[1, 2, 2], [3, 4, 4], [3, 4, 4]], dtype=np.float32))
