# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
dim = 10
n = 50
skip = 17
for dtype in [np.float64, np.float32]:
    sample_noskip = math_ops.sobol_sample(dim, n + skip, dtype=dtype)
    sample_skip = math_ops.sobol_sample(dim, n, skip, dtype=dtype)

    self.assertAllClose(
        self.evaluate(sample_noskip)[skip:, :], self.evaluate(sample_skip))
