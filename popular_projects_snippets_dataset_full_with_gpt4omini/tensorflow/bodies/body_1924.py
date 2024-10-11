# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
img = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               dtype=dtypes.bfloat16.as_numpy_dtype)
self._assertForwardOpMatchesExpected(
    img, [4, 4],
    expected=np.array(
        [[1, 2, 2, 3], [4, 5, 5, 6], [4, 5, 5, 6], [7, 8, 8, 9]],
        dtype=np.float32))
