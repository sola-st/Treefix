# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
"""Statistical test for the gradient.

    The equation (5) of https://arxiv.org/abs/1805.08498 says
      d/dalpha E_{sample ~ Gamma(alpha, 1)} f(sample)
        = E_{sample ~ Gamma(alpha, 1)} df(sample)/dalpha.

    Choose a quadratic loss function f(sample) = (sample - t)^2.
    Then, the lhs can be computed analytically:
      d/dalpha E_{sample ~ Gamma(alpha, 1)} f(sample)
        = d/dalpha [ (alpha + alpha^2) - 2 * t * alpha + t^2 ]
        = 1 + 2 * alpha - 2 * t.

    We compare the Monte-Carlo estimate of the expectation with the
    true gradient.
    """
num_samples = 10000
t = 0.3
alpha = 0.5
expected = 1 + 2 * alpha - 2 * t

alpha = constant_op.constant(alpha)
sample = random_ops.random_gamma([num_samples], alpha, 1.0, seed=12345)
loss = math_ops.reduce_mean(math_ops.square(sample - t))
dloss_dalpha = gradients_impl.gradients(loss, alpha)[0]
dloss_dalpha_val = self.evaluate(dloss_dalpha)
self.assertAllClose(expected, dloss_dalpha_val, atol=1e-1, rtol=1e-1)
