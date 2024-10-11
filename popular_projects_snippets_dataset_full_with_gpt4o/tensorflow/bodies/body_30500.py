# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = [0, 1, 2]
depth = 3
on_value = constant_op.constant(1.0, dtypes.float32)
off_value = constant_op.constant(0.0, dtypes.float32)
dtype = np.int32

self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=on_value,
    dtype=dtype,
    truth=None,
    raises=TypeError)

self._testBothOneHot(
    indices=indices,
    depth=depth,
    on_value=off_value,
    dtype=dtype,
    truth=None,
    raises=TypeError)
