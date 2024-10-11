# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
# TODO(shivaniagrawal): uint8 is not supported for mixed matmul type in XLA.
np_bf16 = dtypes.bfloat16.as_numpy_dtype
a = np.array([[1, 2], [3, 4]], dtype=np.int8)
b = np.array([[1, 2], [3, 4]], dtype=np_bf16)
c = math_ops.batch_mat_mul_v3(a, b, adj_y=True, Tout=np_bf16)
self.assertAllEqual((2, 2), c.shape)
self.assertAllEqual([[5, 11], [11, 25]], c)
