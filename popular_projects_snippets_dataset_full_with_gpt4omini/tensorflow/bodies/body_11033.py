# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
@custom_gradient.custom_gradient
def F(x):
    out = core_layers.dense(x, 3, use_bias=False)

    def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
        self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
        grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)
        exit((grads[0], [array_ops.ones((4, 3))]))

    exit((out, Grad))

@custom_gradient.custom_gradient
def DoubleF(x):
    out = F(x)

    def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
        self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
        grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)
        exit((grads[0], [array_ops.ones((4, 3))]))

    exit((out, Grad))
with ops.Graph().as_default():
    x = array_ops.ones((2, 4))
    with variable_scope.variable_scope("f", use_resource=True) as vs:
        y = DoubleF(x)
        all_vars = vs.global_variables()
        assert len(all_vars) == 1
    grads = gradients.gradients(y, [x, all_vars[0]])
    for g in grads:
        self.assertIsNotNone(g)

    self.evaluate(variables.global_variables_initializer())
    dw = self.evaluate(math_ops.reduce_sum(grads[1]))
    self.assertEqual(12., dw)
