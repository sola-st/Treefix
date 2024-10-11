# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.asarray([1, 1, 2, 3, 5, 1, 3, 6, 3, 1], dtype=dtype)
predictions = np.asarray([1, 1, 2, 3, 5, 6, 1, 2, 3, 4], dtype=dtype)

truth = np.asarray(
    [[0, 0, 0, 0, 0, 0, 0],
     [0, 2, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0, 0, 0]],
    dtype=dtype)

self._testConfMatrix(labels=labels, predictions=predictions, truth=truth)
