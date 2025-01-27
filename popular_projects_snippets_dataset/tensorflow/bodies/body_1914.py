# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
self._assertForwardOpMatchesExpected(
    np.array([[1]], dtype=np.float32), [2, 2],
    expected=np.array([[1, 1], [1, 1]], dtype=np.float32))
