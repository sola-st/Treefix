# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
"""Statistical test for the gradient.

    Using the equation (5) of https://arxiv.org/abs/1805.08498, we have
      1 = d/dalpha E_{sample ~ Gamma(alpha, 1)} sample
        = E_{sample ~ Gamma(alpha, 1)} dsample/dalpha.
    Here we verify that the rhs is fairly close to one.
    The convergence speed is not great, so we use many samples and loose bounds.
    """
num_samples = 10000
alpha = constant_op.constant([0.8, 1e1, 1e3], dtype=dtypes.float32)
sample = random_ops.random_gamma([num_samples], alpha, seed=12345)
# We need to average the gradients, which is equivalent to averaging the
# samples and then doing backprop.
mean_sample = math_ops.reduce_mean(sample, axis=0)
dsample_dalpha = gradients_impl.gradients(mean_sample, alpha)[0]
dsample_dalpha_val = self.evaluate(dsample_dalpha)
self.assertAllClose(dsample_dalpha_val, [1.0] * 3, atol=1e-1, rtol=1e-1)
