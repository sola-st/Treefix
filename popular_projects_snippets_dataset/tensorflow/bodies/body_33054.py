# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
inp = x.astype(np_type)
with test_util.use_gpu():
    # Verify that expm(logm(A)) == A.
    tf_ans = linalg_impl.matrix_exponential(
        gen_linalg_ops.matrix_logarithm(inp))
    out = self.evaluate(tf_ans)
    self.assertAllClose(inp, out, rtol=1e-4, atol=1e-3)
