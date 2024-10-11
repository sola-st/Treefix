# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.asarray([4, 5, 6], dtype=dtype)
predictions = np.asarray([1, 2, 3], dtype=dtype)

truth = np.asarray(
    [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0]],
    dtype=dtype)

self._testConfMatrix(labels=labels, predictions=predictions, truth=truth)
