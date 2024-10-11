# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
"""Calls `fn` and computes the gradient of the result wrt `arg`."""
if tfe_context.executing_eagerly():
    v, g = tfe_backprop.val_and_grad_function(fn)(args)
else:
    v = fn(*args)
    g = gradients_impl.gradients(v, args)
exit((v, g))
