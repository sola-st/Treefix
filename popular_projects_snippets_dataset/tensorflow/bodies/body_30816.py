# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
# We create 2 batches of logits for testing.
# batch 0 is the boring uniform distribution: 1, 1, 1, 1, with target 3.
# batch 1 has a bit of difference: 1, 2, 3, 4, with soft targets (1, 2).
logits = [[1., 1., 1., 1.], [1., 2., 3., 4.]]
labels = [[0., 0., 0., 1.], [0., .5, .5, 0.]]

# For batch 0, we expect the uniform distribution: 0.25, 0.25, 0.25, 0.25
# With a hard target 3, the gradient is [0.25, 0.25, 0.25, -0.75]
# The loss for this batch is -log(0.25) = 1.386
#
# For batch 1, we have:
# exp(0) = 1
# exp(1) = 2.718
# exp(2) = 7.389
# exp(3) = 20.085
# SUM = 31.192
# So we have as probabilities:
# exp(0) / SUM = 0.032
# exp(1) / SUM = 0.087
# exp(2) / SUM = 0.237
# exp(3) / SUM = 0.644
# With a soft target (1, 2), the gradient is
# [0.032, 0.087 - 0.5 = -0.413, 0.237 - 0.5 = -0.263, 0.644]
# The loss for this batch is [0.5 * -log(0.087), 0.5 * -log(0.237)]
# = [1.3862, 1.9401]
np_loss, np_gradient = self._npXent(np.array(labels), np.array(logits))
self.assertAllClose(
    np.array([[0.25, 0.25, 0.25, -0.75], [0.0321, -0.4129, -0.2632,
                                          0.6439]]),
    np_gradient,
    rtol=1.e-3,
    atol=1.e-3)
self.assertAllClose(
    np.array([1.3862, 1.9401]), np_loss, rtol=1.e-3, atol=1.e-3)
