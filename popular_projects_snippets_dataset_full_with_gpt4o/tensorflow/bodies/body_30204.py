# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
t = np.broadcast_to(np.arange(0, 7), (3, 2, 1, 7))
paddings = constant_op.constant([
    [1, 1],
    [0, 0],
    [0, 0],
    [2, 2],
])
expected = np.broadcast_to(np.array([9, 27, 27]), (1, 2, 1, 3))
result = gen_array_ops.mirror_pad_grad(t, paddings, "SYMMETRIC")
self.assertAllEqual(result, expected)
