# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
np.random.seed(42)
size = 1000
inp = np.random.randint(0, size, (4096), dtype=dtype)
np_out = np.bincount(inp, minlength=size)
with test_util.use_gpu():
    self.assertAllEqual(
        np_out,
        self.evaluate(
            gen_math_ops.dense_bincount(input=inp, weights=[], size=size)))
