# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
self.setUp()
with self.session(use_gpu=use_gpu):
    var = variables.VariableV1(x)
    accum = variables.VariableV1(y)
    self.evaluate(variables.global_variables_initializer())

    self.assertAllCloseAccordingToType(x, self.evaluate(var))
    apply_adagrad = training_ops.apply_adagrad(var, accum, lr, grad)
    out = self.evaluate(apply_adagrad)
    self.assertShapeEqual(out, apply_adagrad)
    self.assertAllCloseAccordingToType(x - lr * grad * (y + grad * grad)**
                                       (-0.5), out)
    self.assertAllCloseAccordingToType(y + grad * grad, self.evaluate(accum))
