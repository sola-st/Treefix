# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
t = np.broadcast_to(np.reshape(np.arange(0, 7), (7, 1)), (1, 4, 7, 1))
paddings = constant_op.constant([
    [0, 0],
    [1, 1],
    [2, 2],
    [0, 0],
])
expected = np.broadcast_to(
    np.reshape(np.array([16, 18, 8]), (3, 1)), (1, 2, 3, 1))
result = gen_array_ops.mirror_pad_grad(t, paddings, "REFLECT")
self.assertAllEqual(result, expected)
