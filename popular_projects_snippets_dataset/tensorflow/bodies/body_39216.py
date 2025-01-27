# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
x = np.ones((4, 0)).astype(np.float32)
y = np.ones((0, 3)).astype(np.float32)
for x_dtype in (dtypes.float32, dtypes.bfloat16):
    for y_dtype in (dtypes.float32, dtypes.bfloat16):
        self._testCpuMatmul(x, y, x_dtype=x_dtype, y_dtype=y_dtype)
