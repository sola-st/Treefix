# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
for tr_a in [True, False]:
    for tr_b in [True, False]:
        for sp_a in [True, False]:
            for sp_b in [True, False]:
                for a_dtype in (dtypes.float32, dtypes.bfloat16):
                    for b_dtype in (dtypes.float32, dtypes.bfloat16):
                        # Note: bfloat16 only has 7 mantissa bits, versus float32 with
                        # 10. Hence, we shift by 2 bits to pass the test.
                        if a_dtype == dtypes.bfloat16 and b_dtype == dtypes.bfloat16:
                            delta = 1 / 16.
                        else:
                            delta = 1 / 64.
                        name = "sparse_matmul_%s_%s_%s_%s" % (tr_a, tr_b, sp_a, sp_b)
                        self._testGradients(tr_a, tr_b, sp_a, sp_b, a_dtype, b_dtype,
                                            delta, name)
