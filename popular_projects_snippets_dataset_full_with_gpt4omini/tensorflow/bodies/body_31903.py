# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
super(CosineDistanceLossTest, self).setUp()
self._predictions = np.asarray([
    [1, 0, 0],  # Batch 1
    [0, 0, -1],
    [1, 0, 0],  # Batch 2
    [1, 0, 0],
    [0, 0, -1],  # Batch 3
    [1, 0, 0]
]).reshape((3, 2, 3))

self._labels = np.asarray([[1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0],
                           [0, 0, 1], [0, 1, 0]]).reshape((3, 2, 3))
