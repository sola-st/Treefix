# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
for itype in [dtypes.int32, dtypes.int64, dtypes.uint8]:
    prefix_dim_size = 65536
    depth = 2
    x = [i % depth for i in range(prefix_dim_size)]
    indices = constant_op.constant(x, dtype=itype)

    truth = np.zeros((prefix_dim_size, depth), np.float32)
    for i in range(prefix_dim_size):
        truth[i, x[i]] = 1.0

    self._testBothOneHot(
        indices=indices,
        depth=depth,
        on_value=1.0,
        off_value=0.0,
        truth=truth)
