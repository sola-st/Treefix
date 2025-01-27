# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# Test that we don't differentiate 'x'. The gradient function for 'x' is
# set explicitly to None so we will get an exception if the gradient code
# tries to differentiate 'x'.
with ops.Graph().as_default():
    c = constant(1.0)
    x = array_ops.identity(c)
    y = x + 1.0
    z = y + 1
    grads = gradients.gradients(z, [x])
    self.assertTrue(all(x is not None for x in grads))
