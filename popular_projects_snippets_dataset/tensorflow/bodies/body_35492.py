# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
for dt in dtypes.float16, dtypes.float32, dtypes.float64:
    sx = stateless_random_ops.stateless_random_binomial(
        shape=[1000], seed=[12, 34], counts=10., probs=0.4, output_dtype=dt)
    sy = stateless_random_ops.stateless_random_binomial(
        shape=[1000], seed=[12, 34], counts=10., probs=0.4, output_dtype=dt)
    sx0, sx1 = self.evaluate(sx), self.evaluate(sx)
    sy0, sy1 = self.evaluate(sy), self.evaluate(sy)
    self.assertAllEqual(sx0, sx1)
    self.assertAllEqual(sx0, sy0)
    self.assertAllEqual(sy0, sy1)
