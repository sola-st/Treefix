# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0, dtype=dtype)
    var = variables.Variable(init)
    dummy_const = constant_op.constant(0.0)
    gradient = gradients.gradients(
        dummy_const,
        var,
        unconnected_gradients=unconnected_gradients.UnconnectedGradients.ZERO
    )[0]
    self.assertEqual(gradient.dtype, dtype)
    self.assertIsNotNone(gradient)
