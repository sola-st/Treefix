# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = np.array([[1., 2, 3],
                  [2.5, 4, 0.01]], dtype=np.float32)
dist = dirichlet_lib.Dirichlet(alpha)  # batch_shape=[2], event_shape=[3]
x = dist.sample(int(250e3), seed=1)
sample_mean = math_ops.reduce_mean(x, 0)
x_centered = x - sample_mean[None, ...]
sample_cov = math_ops.reduce_mean(math_ops.matmul(
    x_centered[..., None], x_centered[..., None, :]), 0)
sample_var = array_ops.matrix_diag_part(sample_cov)
sample_stddev = math_ops.sqrt(sample_var)

[
    sample_mean_,
    sample_cov_,
    sample_var_,
    sample_stddev_,
    analytic_mean,
    analytic_cov,
    analytic_var,
    analytic_stddev,
] = self.evaluate([
    sample_mean,
    sample_cov,
    sample_var,
    sample_stddev,
    dist.mean(),
    dist.covariance(),
    dist.variance(),
    dist.stddev(),
])

self.assertAllClose(sample_mean_, analytic_mean, atol=0.04, rtol=0.)
self.assertAllClose(sample_cov_, analytic_cov, atol=0.06, rtol=0.)
self.assertAllClose(sample_var_, analytic_var, atol=0.04, rtol=0.)
self.assertAllClose(sample_stddev_, analytic_stddev, atol=0.02, rtol=0.)
