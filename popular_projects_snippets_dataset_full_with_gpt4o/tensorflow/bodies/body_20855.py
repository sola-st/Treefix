# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
self.setUp()
with self.session(use_gpu=use_gpu):
    var = variables.VariableV1(x)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllCloseAccordingToType(x, self.evaluate(var))
    apply_sgd = training_ops.apply_gradient_descent(var, alpha, delta)
    out = self.evaluate(apply_sgd)
    self.assertShapeEqual(out, apply_sgd)
    self.assertAllCloseAccordingToType(x - alpha * delta, out)
