# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
np.random.seed(42)
inp = np.random.randint(0, size, (num_rows, num_cols), dtype=dtype)
np_weight = np.random.random((num_rows, num_cols))
np_out = np.reshape(
    np.concatenate([
        np.bincount(inp[j, :], weights=np_weight[j, :], minlength=size)
        for j in range(num_rows)
    ],
                   axis=0), (num_rows, size))
with test_util.use_gpu():
    evaluated = self.evaluate(
        gen_math_ops.dense_bincount(input=inp, weights=np_weight, size=size))
    if np_out.dtype in (np.float32, np.float64):
        self.assertAllClose(np_out, evaluated)
    else:
        self.assertAllEqual(np_out, evaluated)
