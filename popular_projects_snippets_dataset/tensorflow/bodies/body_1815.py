# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
self._testNAryLists(array_ops.identity_n,
                    [np.array([[1, 2, 3]], dtype=np.float32)],
                    expected=[np.array([[1, 2, 3]], dtype=np.float32)])
self._testNAryLists(array_ops.identity_n,
                    [np.array([[1, 2], [3, 4]], dtype=np.float32),
                     np.array([[3, 2, 1], [6, 5, 1]], dtype=np.float32)],
                    expected=[
                        np.array([[1, 2], [3, 4]], dtype=np.float32),
                        np.array([[3, 2, 1], [6, 5, 1]], dtype=np.float32)])
self._testNAryLists(array_ops.identity_n,
                    [np.array([[1], [2], [3], [4]], dtype=np.int32),
                     np.array([[3, 2, 1], [6, 5, 1]], dtype=np.float32)],
                    expected=[
                        np.array([[1], [2], [3], [4]], dtype=np.int32),
                        np.array([[3, 2, 1], [6, 5, 1]], dtype=np.float32)])
