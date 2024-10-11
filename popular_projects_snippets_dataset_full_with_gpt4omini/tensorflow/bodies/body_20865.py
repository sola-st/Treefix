# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
self.setUp()
with self.session(use_gpu=False):
    var = variables.VariableV1(x)
    accum = variables.VariableV1(y)
    linear = variables.VariableV1(z)
    self.evaluate(variables.global_variables_initializer())

    self.assertAllCloseAccordingToType(x, self.evaluate(var))
    sparse_apply_ftrl = (
        training_ops.sparse_apply_ftrl(
            var,
            accum,
            linear,
            grad,
            constant_op.constant(indices, self._toType(indices.dtype)),
            lr,
            l1,
            l2,
            lr_power=lr_power,
            multiply_linear_by_lr=True))
    out = self.evaluate(sparse_apply_ftrl)
    self.assertShapeEqual(out, sparse_apply_ftrl)

    for (i, index) in enumerate(indices):
        self.assertAllCloseAccordingToType(
            x[index] - lr * grad[i] * (y[index] + grad[i] * grad[i])**
            (lr_power),
            self.evaluate(var)[index])
        self.assertAllCloseAccordingToType(y[index] + grad[i] * grad[i],
                                           self.evaluate(accum)[index])
