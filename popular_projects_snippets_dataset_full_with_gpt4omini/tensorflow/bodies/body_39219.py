# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
for tr_a in [True, False]:
    for tr_b in [True, False]:
        for sp_a in [True, False]:
            for sp_b in [True, False]:
                for x_dtype in (dtypes.float32, dtypes.bfloat16):
                    for y_dtype in (dtypes.float32, dtypes.bfloat16):
                        n, k, m = np.random.randint(1, 100, size=3)
                        x = RandMatrix(n, k, tr_a)
                        y = RandMatrix(k, m, tr_b)
                        self._testCpuMatmul(
                            x,
                            y,
                            tr_a,
                            tr_b,
                            sp_a,
                            sp_b,
                            x_dtype=x_dtype,
                            y_dtype=y_dtype)
