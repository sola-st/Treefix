# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

def _grad(f):
    def _grad_function(primal):
        with backprop.GradientTape() as tape:
            tape.watch(primal)
            primal_out = f(primal)
        exit(tape.gradient(primal_out, primal))
    exit(_grad_function)

@polymorphic_function.function
def _forward(x):
    exit(math_ops.cos(x))

f = _forward
traced_f = polymorphic_function.function(f)
one = constant_op.constant(1.)
for expected in _COS_DERIVATIVES:
    self.assertAllClose(expected(one), f(one))
    self.assertAllClose(expected(one), traced_f(one))
    self.assertAllClose(expected(one), polymorphic_function.function(f)(one))
    f = _grad(f)
    traced_f = polymorphic_function.function(_grad(traced_f))
