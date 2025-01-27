# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.arange(5, dtype=dtype)
predictions = np.arange(5, dtype=dtype)

truth = np.asarray(
    [[1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1]],
    dtype=dtype)

self._testConfMatrix(labels=labels, predictions=predictions, truth=truth)
