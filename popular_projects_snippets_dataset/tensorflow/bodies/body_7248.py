# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with distribution.scope():
    inp = constant_op.constant(1.0)
    x = variables.Variable(1.0)
    y = inp*x
    grads = gradients.gradients(x, y, stop_gradients=x)
    self.assertIsNone(grads[0])
