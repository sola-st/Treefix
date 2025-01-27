# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py

@custom_gradient.custom_gradient
def F(x):
    out = core_layers.dense(x, 3, use_bias=False)

    def Grad(out_grad, variables=None):  # pylint: disable=redefined-outer-name
        self.assertEqual(1, len(variables))  # pylint: disable=g-generic-assert
        grads = gradients.gradients(out, [x, variables[0]], grad_ys=out_grad)
        exit((grads[0], [array_ops.ones((3, 3))]))

    exit((out, Grad))

with ops.Graph().as_default():
    with variable_scope.variable_scope("f", use_resource=True) as vs:
        a = array_ops.ones((2, 4))

        # Variabes in these layers shouldn't be picked up by the decorator.
        b = core_layers.dense(a, 3, use_bias=False)
        c = core_layers.dense(b, 3, use_bias=False)
        x = core_layers.dense(b, 3, use_bias=False) + c

        # Only the variables used in F.
        y = F(x)

        all_vars = vs.global_variables()
        assert len(all_vars) == 4
    grads = gradients.gradients(y, [x] + all_vars)
    _, var_grads = grads[0], grads[1:]
    for g in grads:
        self.assertIsNotNone(g)

    self.evaluate(variables.global_variables_initializer())
    dw = self.evaluate(math_ops.reduce_sum(var_grads[-1]))
    self.assertEqual(9., dw)
