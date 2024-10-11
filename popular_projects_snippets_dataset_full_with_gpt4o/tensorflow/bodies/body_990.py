# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
self._assertOpOutputMatchesExpected(
    array_ops.unstack,
    np.array([[1., 2.], [3., 4.], [5., 6.]], dtype=np.float32),
    expected=[
        np.array([1., 2.], dtype=np.float32),
        np.array([3., 4.], dtype=np.float32),
        np.array([5., 6.], dtype=np.float32),
    ],
    equality_test=self.ListsAreClose)

self._assertOpOutputMatchesExpected(
    lambda x: array_ops.unstack(x, axis=1),
    np.array([[1., 2.], [3., 4.], [5., 6.]], dtype=np.float32),
    expected=[
        np.array([1., 3., 5.], dtype=np.float32),
        np.array([2., 4., 6.], dtype=np.float32),
    ],
    equality_test=self.ListsAreClose)
