# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0)
    var = variables.Variable(init)
    gradient = gradients.gradients(var.read_value(), var)
    self.assertIsNotNone(gradient)
