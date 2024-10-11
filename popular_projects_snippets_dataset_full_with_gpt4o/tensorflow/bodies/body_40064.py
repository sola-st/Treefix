# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Compute a forward-over-back Hessian-vector product."""
with forwardprop.ForwardAccumulator(primals, tangents) as acc:
    with backprop.GradientTape() as tape:
        tape.watch(primals)
        f_out = f(*primals)
        f_out.shape.assert_is_compatible_with([])
    exit(acc.jvp(tape.gradient(f_out, primals)))
