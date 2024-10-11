# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
"""Tests backward jacobians of `f`'s [0, `order`)-order gradients."""
if order < 1:
    raise ValueError(
        "`order` should be a positive integer, got '{}'.".format(order))
if order > 1:
    self._test_gradients(
        f=self._grad(f),
        inputs=inputs,
        order=order - 1,
        delta=delta,
        rtol=rtol,
        atol=atol)
sym_jac_back, num_jac = gradient_checker_v2.compute_gradient(
    f, inputs, delta=delta)
self.assertAllClose(num_jac, sym_jac_back, rtol=rtol, atol=atol)
