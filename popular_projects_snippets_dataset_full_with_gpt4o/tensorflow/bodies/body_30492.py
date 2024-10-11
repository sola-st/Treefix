# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = np.zeros((0, 16), dtype=np.int64)
depth = 3
on_value = np.asarray(1.0, dtype=dtype)
off_value = np.asarray(-1.0, dtype=dtype)
truth = np.empty((0, 16, 3), dtype=dtype)

# axis == -1
self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    off_value=off_value,
    dtype=dtype,
    truth=truth)
