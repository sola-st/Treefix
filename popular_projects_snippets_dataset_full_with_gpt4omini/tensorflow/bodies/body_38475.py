# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.arange(5, dtype=np.int32)
predictions = np.arange(5, dtype=np.int32)
weights = np.arange(5, dtype=np.int32)

truth = np.asarray(
    [[0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 2, 0, 0],
     [0, 0, 0, 3, 0],
     [0, 0, 0, 0, 4]],
    dtype=np.int32)

self._testConfMatrix(
    labels=labels, predictions=predictions, weights=weights, truth=truth)
