# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
self.setUp()
with self.session(use_gpu=use_gpu):
    var = variables.VariableV1(x)
    accum = variables.VariableV1(y)
    self.evaluate(variables.global_variables_initializer())

    self.assertAllCloseAccordingToType(x, self.evaluate(var))
    sparse_apply_adagrad = training_ops.sparse_apply_adagrad(
        var, accum, lr, grad,
        constant_op.constant(indices, self._toType(indices.dtype)))
    out = self.evaluate(sparse_apply_adagrad)
    self.assertShapeEqual(out, sparse_apply_adagrad)

    for (i, index) in enumerate(indices):
        self.assertAllCloseAccordingToType(
            x[index] - lr * grad[i] * (y[index] + grad[i] * grad[i])**(-0.5),
            self.evaluate(var)[index])
        self.assertAllCloseAccordingToType(y[index] + grad[i] * grad[i],
                                           self.evaluate(accum)[index])
