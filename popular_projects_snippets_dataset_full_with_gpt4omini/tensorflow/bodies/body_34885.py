# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
with self.cached_session() as sess:
    dist = ds.DirichletMultinomial(
        total_count=5.,
        concentration=1. + 2. * self._rng.rand(4, 3, 2).astype(np.float32))
    n = int(3e3)
    x = dist.sample(n, seed=0)
    sample_mean = math_ops.reduce_mean(x, 0)
    # Cyclically rotate event dims left.
    x_centered = array_ops.transpose(x - sample_mean, [1, 2, 3, 0])
    sample_covariance = math_ops.matmul(
        x_centered, x_centered, adjoint_b=True) / n
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
    self.assertAllEqual([4, 3, 2], sample_mean.get_shape())
    self.assertAllClose(actual_mean_, sample_mean_, atol=0., rtol=0.20)
    self.assertAllEqual([4, 3, 2, 2], sample_covariance.get_shape())
    self.assertAllClose(
        actual_covariance_, sample_covariance_, atol=0., rtol=0.20)
