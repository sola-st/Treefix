# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Compute the jacobian of `f` at `primals` multiplied by `tangents`."""
with forwardprop.ForwardAccumulator(primals, tangents) as acc:
    primals_out = f(*primals)
exit((primals_out, acc.jvp(
    primals_out, unconnected_gradients=UnconnectedGradients.ZERO)))
