# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
self._testNAry(lambda x: array_ops.strided_slice(*x),
               [np.array([[], [], []], dtype=np.float32),
                np.array([1, 0], dtype=np.int32),
                np.array([3, 0], dtype=np.int32),
                np.array([1, 1], dtype=np.int32)],
               expected=np.array([[], []], dtype=np.float32))

if np.int64 in self.int_types:
    self._testNAry(
        lambda x: array_ops.strided_slice(*x), [
            np.array([[], [], []], dtype=np.float32), np.array(
                [1, 0], dtype=np.int64), np.array([3, 0], dtype=np.int64),
            np.array([1, 1], dtype=np.int64)
        ],
        expected=np.array([[], []], dtype=np.float32))

self._testNAry(lambda x: array_ops.strided_slice(*x),
               [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                         dtype=np.float32),
                np.array([1, 1], dtype=np.int32),
                np.array([3, 3], dtype=np.int32),
                np.array([1, 1], dtype=np.int32)],
               expected=np.array([[5, 6], [8, 9]], dtype=np.float32))

self._testNAry(lambda x: array_ops.strided_slice(*x),
               [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                         dtype=np.float32),
                np.array([0, 2], dtype=np.int32),
                np.array([2, 0], dtype=np.int32),
                np.array([1, -1], dtype=np.int32)],
               expected=np.array([[3, 2], [6, 5]], dtype=np.float32))

self._testNAry(lambda x: x[0][0:2, array_ops.newaxis, ::-1],
               [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                         dtype=np.float32)],
               expected=np.array([[[3, 2, 1]], [[6, 5, 4]]],
                                 dtype=np.float32))

self._testNAry(lambda x: x[0][1, :, array_ops.newaxis],
               [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                         dtype=np.float32)],
               expected=np.array([[4], [5], [6]], dtype=np.float32))
