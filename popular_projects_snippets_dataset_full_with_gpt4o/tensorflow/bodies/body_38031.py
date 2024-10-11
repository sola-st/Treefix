# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
# TODO(shivaniagrawal): uint8 is not supported for mixed matmul type in XLA.
for (a_dtype, b_dtype) in [(np.int8, np.int8), (np.uint8, np.uint8)]:
    a = np.array([[1, 2], [3, 4]], dtype=a_dtype)
    b = np.array([[1, 2], [3, 4]], dtype=b_dtype)
    c = math_ops.batch_mat_mul_v3(a, b, adj_y=True, Tout=np.int32)
    self.assertAllEqual((2, 2), c.shape)
    self.assertAllEqual([[5, 11], [11, 25]], c)
