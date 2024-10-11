# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = [0, 1, 2]
depth = 3
on_value = np.asarray(1.0, np.float64)
off_value = np.asarray(0.0, np.float32)

self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    off_value=off_value,
    truth=None,
    raises=TypeError)
