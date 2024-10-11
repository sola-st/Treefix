# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = np.asarray([[0, 2, -1, 1], [1, 0, 1, -1]], dtype=np.int64)
depth = 3

truth = np.asarray(
    [[[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
     [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]]],
    dtype=dtype)

# axis == -1
self._testBothOneHot(indices=indices, depth=depth, dtype=dtype, truth=truth)

# axis == 1
self._testBothOneHot(
    indices=indices,
    depth=depth,
    axis=1,
    dtype=dtype,
    truth=[truth[0].T, truth[1].T])  # Do not transpose the batch
