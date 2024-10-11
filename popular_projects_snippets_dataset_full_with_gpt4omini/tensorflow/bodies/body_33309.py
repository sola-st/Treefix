# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
inp = x.astype(np_type)
with test_util.use_gpu():
    tf_ans = linalg_impl.matrix_exponential(inp)
    if x.size == 0:
        np_ans = np.empty(x.shape, dtype=np_type)
    else:
        if x.ndim > 2:
            np_ans = np.zeros(inp.shape, dtype=np_type)
            for i in itertools.product(*[range(x) for x in inp.shape[:-2]]):
                np_ans[i] = np_expm(inp[i])
        else:
            np_ans = np_expm(inp)
    out = self.evaluate(tf_ans)
    self.assertAllClose(np_ans, out, rtol=1e-3, atol=1e-3)
