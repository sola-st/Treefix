# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
r1 = np.random.randint(6000, 20000)
r2 = np.random.randint(1, 10)
r3 = np.random.randint(1, 10)
for m, k, n in [(r1, r2, r3), (r2, r1, r3), (r2, r3, r1)]:
    for x_dtype in (dtypes.float32, dtypes.bfloat16):
        for y_dtype in (dtypes.float32, dtypes.bfloat16):
            x = RandMatrix(m, k, False)
            y = RandMatrix(k, n, False)
            self._testCpuMatmul(x, y, x_dtype=x_dtype, y_dtype=y_dtype)
