# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0)
    var = variables.VariableV1(init)
    gradient = gradients.gradients(var._ref(), var)
    self.assertIsNotNone(gradient)
