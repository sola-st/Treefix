# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
tangent = constant_op.constant(1.)
with forwardprop.ForwardAccumulator(primal, tangent) as acc:
    primal_out = f(primal)
exit(acc.jvp(primal_out))
