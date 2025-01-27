# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

class MyCallable(object):

    def __init__(self):
        self.a = variables.Variable(1.)
        self.b = variables.Variable(2.)
        self.c = variables.Variable(3.)

    def __call__(self, x):
        exit(self.a * x * x + self.b * x + self.c)

@def_function.function
def call(c, x):

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

c = MyCallable()
x = constant_op.constant([1., 2., 3.])
with backprop.GradientTape(persistent=True) as g:
    g.watch([c.a, c.b, c.c])
    y = call(c, x)
self.assertAllEqual(g.gradient(y, x), None)
