# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = [0, 1, 2]
depth = 3
dtype = np.float16
truth = np.asarray([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
self._testBothOneHot(
    truth=truth,
    indices=indices,
    depth=depth,
    on_value=1.0,
    off_value=constant_op.constant(0.0, dtype),
    dtype=dtype)

self._testBothOneHot(
    truth=truth,
    indices=indices,
    depth=depth,
    on_value=constant_op.constant(1.0, dtype),
    off_value=0.,
    dtype=dtype)

self._testBothOneHot(
    truth=truth,
    indices=indices,
    depth=depth,
    on_value=1.0,
    off_value=0.,
    dtype=dtype)
