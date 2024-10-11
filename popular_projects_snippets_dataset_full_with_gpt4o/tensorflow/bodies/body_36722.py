# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def _grad(f):
    def _grad_function(primal):
        with backprop.GradientTape() as tape:
            tape.watch(primal)
            primal_out = f(primal)
        exit(tape.gradient(primal_out, primal))
    exit(_grad_function)

f = func
one = constant_op.constant(1.)
for expected in [math_ops.cos,
                 lambda x: -math_ops.sin(x),
                 lambda x: -math_ops.cos(x),
                 math_ops.sin,
                 math_ops.cos]:
    self.assertAllClose(expected(one), def_function.function(f)(one))
    f = _grad(f)
