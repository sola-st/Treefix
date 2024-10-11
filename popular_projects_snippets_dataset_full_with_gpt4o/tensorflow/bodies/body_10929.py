# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    #  a    b
    #  |    |
    # IdentityN
    #  |    |
    #  c    d
    #  |    |
    #  SG   |
    #  |    |
    #   \  /
    #    +
    #    e
    a = constant_op.constant(1.0)
    b = constant_op.constant(1.0)
    c, d = array_ops.identity_n([a, b])
    e = array_ops.stop_gradient(c) + d
    # The aggregated grads for the IdentityN node would look like
    # [None, Tensor]. We expect this None to be converted to zeros.
    output = gradients.gradients(
        e, c, unconnected_gradients=unconnected_gradients_val)
    if (unconnected_gradients_val ==
        unconnected_gradients.UnconnectedGradients.ZERO):
        self.assertIsNotNone(output[0])
    else:
        self.assertIsNone(output[0])
