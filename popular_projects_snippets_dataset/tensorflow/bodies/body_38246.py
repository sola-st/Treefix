# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
np.random.seed(42)
inp = np.random.randint(0, size, (num_rows, num_cols), dtype=dtype)
np_out = np.reshape(
    np.concatenate(
        [np.bincount(inp[j, :], minlength=size) for j in range(num_rows)],
        axis=0), (num_rows, size))
with test_util.use_gpu():
    self.assertAllEqual(
        np_out,
        self.evaluate(
            gen_math_ops.dense_bincount(input=inp, weights=[], size=size)))
