# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
shape = []
alpha = array_ops.ones([2, 2])
beta = array_ops.ones([1, 2])
sample = random_ops.random_gamma(shape, alpha, beta, seed=12345)
grads_alpha, grads_beta = gradients_impl.gradients(sample, [alpha, beta])
self.assertAllEqual(grads_alpha.shape, alpha.shape)
self.assertAllEqual(grads_beta.shape, beta.shape)
