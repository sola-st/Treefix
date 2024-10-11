# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Tests forward/backward jacobians of `f`'s [0, `order`)-order gradients."""
if order < 1:
    raise ValueError(
        "`order` should be a positive integer, got '{}'.".format(order))
if order > 1:
    _test_gradients(
        testcase=testcase,
        f=_grad(f),
        primals=primals,
        order=order - 1,
        delta=delta,
        rtol=rtol,
        atol=atol,
        srtol=srtol,
        satol=satol)
sym_jac_back, num_jac = gradient_checker_v2.compute_gradient(
    f, primals, delta=delta)
testcase.assertAllClose(num_jac, sym_jac_back, rtol=rtol, atol=atol)
sym_jac_fwd = _jacfwd(f, primals)
testcase.assertAllClose(num_jac, sym_jac_fwd, rtol=rtol, atol=atol)
# And the symbolic computations should be much closer.
testcase.assertAllClose(sym_jac_back, sym_jac_fwd, rtol=srtol, atol=satol)
