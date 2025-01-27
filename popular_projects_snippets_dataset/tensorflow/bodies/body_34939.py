# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session() as sess:
    dist = multinomial.Multinomial(
        total_count=5.,
        logits=math_ops.log(2. * self._rng.rand(4).astype(np.float32)))
    n = int(5e3)
    x = dist.sample(n, seed=0)
    sample_mean = math_ops.reduce_mean(x, 0)
    x_centered = x - sample_mean  # Already transposed to [n, 2].
    sample_covariance = math_ops.matmul(
        x_centered, x_centered, adjoint_a=True) / n
    [
        sample_mean_,
        sample_covariance_,
        actual_mean_,
        actual_covariance_,
    ] = sess.run([
        sample_mean,
        sample_covariance,
        dist.mean(),
        dist.covariance(),
    ])
    self.assertAllEqual([4], sample_mean.get_shape())
    self.assertAllClose(actual_mean_, sample_mean_, atol=0., rtol=0.10)
    self.assertAllEqual([4, 4], sample_covariance.get_shape())
    self.assertAllClose(
        actual_covariance_, sample_covariance_, atol=0., rtol=0.20)
