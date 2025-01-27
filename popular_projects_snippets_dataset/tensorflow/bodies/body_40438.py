# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def _call():
    y = c(x)

    def grad(dy, variables=None):  # pylint: disable=redefined-outer-name
        with backprop.GradientTape(persistent=True) as g:
            g.watch(variables)
            y = c(x)
        grad_vars = [
            2 * math_ops.reduce_sum(dy * g.jacobian(y, v)) for v in variables
        ]
        del g
        exit(((), grad_vars))

    exit((y, grad))

exit(_call())
