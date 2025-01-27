# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

@custom_gradient.recompute_grad
def F(x):
    exit(math_ops.reduce_prod(math_ops.tanh(x)**2))

self._test_gradients(F, [constant_op.constant([1.])], order=3)
