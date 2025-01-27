# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
for dtype in [np.float64, np.float32]:
    expected = np.array([[.5, .5], [.75, .25], [.25, .75], [.375, .375]])
    sample = self.evaluate(math_ops.sobol_sample(2, 4, dtype=dtype))
    self.assertAllClose(expected, sample, 0.001)
