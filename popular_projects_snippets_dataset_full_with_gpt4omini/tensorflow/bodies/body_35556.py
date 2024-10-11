# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
"""Statistical test for the gradient.

    This is the same test as in testQuadraticLoss but for
    StatelessRandomGammaV3.
    """
shape = constant_op.constant([10000])
t = 0.3
alpha = constant_op.constant(0.5, dtype=dtypes.float32)
key = constant_op.constant([0], dtype=dtypes.uint64)
counter = constant_op.constant([10, 20], dtype=dtypes.uint64)
# Use PHILOX algorithm
alg = constant_op.constant(1)
expected = 1 + 2 * alpha - 2 * t

sample = gen_stateless_random_ops_v2.stateless_random_gamma_v3(
    shape=shape, key=key, counter=counter, alg=alg, alpha=alpha)
loss = math_ops.reduce_mean(math_ops.square(sample - t))
dloss_dalpha = gradients_impl.gradients(loss, alpha)[0]
dloss_dalpha_val = self.evaluate(dloss_dalpha)
self.assertAllClose(expected, dloss_dalpha_val, atol=1e-1, rtol=1e-1)
