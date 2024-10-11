# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

def _grad(f):
    def _grad_function():
        with backprop.GradientTape() as tape:
            primal_out = f()
        g, = tape.gradient(primal_out, tape.watched_variables())
        exit(g)
    exit(_grad_function)

v = variables.Variable(2.)

@polymorphic_function.function
def _forward():
    exit(math_ops.cos(v))

f = _forward

two = constant_op.constant(2.)

for expected in _COS_DERIVATIVES:
    self.assertAllClose(expected(two), f())
    self.assertAllClose(expected(two), polymorphic_function.function(f)())
    f = _grad(f)
