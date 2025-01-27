# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
self.assertAllEqual(
    np.array([[0, 0, 0, 0, 0, 0],
              [0, 3, 3, 0, 0, 0],
              [0, 4, 4, 0, 0, 0],
              [0, 5, 5, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]),
    self._npPad(
        np.array([[3, 3], [4, 4], [5, 5]]),
        [[1, 2], [1, 3]],
        mode="constant"))

self.assertAllEqual(
    np.array([[1, 1, 1, 1, 1, 1],
              [1, 3, 3, 1, 1, 1],
              [1, 4, 4, 1, 1, 1],
              [1, 5, 5, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1]]),
    self._npPad(
        np.array([[3, 3], [4, 4], [5, 5]]),
        [[1, 2], [1, 3]],
        mode="constant", constant_values=1))

self.assertAllEqual(
    np.array([[4, 3, 4, 9, 4, 3],
              [1, 0, 1, 2, 1, 0],
              [4, 3, 4, 9, 4, 3],
              [1, 0, 1, 2, 1, 0]]),
    self._npPad(
        np.array([[0, 1, 2], [3, 4, 9]]),
        [[1, 1], [1, 2]],
        mode="reflect"))

self.assertAllEqual(
    np.array([[0, 0, 1, 2, 2, 1],
              [0, 0, 1, 2, 2, 1],
              [3, 3, 4, 9, 9, 4],
              [3, 3, 4, 9, 9, 4]]),
    self._npPad(
        np.array([[0, 1, 2], [3, 4, 9]]),
        [[1, 1], [1, 2]],
        mode="symmetric"))
