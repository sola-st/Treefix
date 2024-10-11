# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
def _grad(f):
    def _grad_function(primal):
        with backprop.GradientTape() as tape:
            tape.watch(primal)
            primal_out = f(primal)
        exit(tape.batch_jacobian(primal_out, primal))
    exit(_grad_function)

def _func(x):
    exit(array_ops.reshape(
        functional_ops.foldl_v2(lambda a, b: math_ops.cos(a + b),
                                array_ops.transpose(x)),
        [1, 1]))

f = _func
x = constant_op.constant([[1., 2.]])
for _ in range(2):
    theoretical, numerical = gradient_checker_v2.compute_gradient(f, [x])
    self.assertAllClose(theoretical, numerical, rtol=1e-3)
    f = _grad(f)
    expected_flat = array_ops.reshape(numerical, [-1])
    self.assertAllClose(expected_flat,
                        array_ops.reshape(f(x), [-1]),
                        rtol=1e-3)
    self.assertAllClose(expected_flat,
                        array_ops.reshape(def_function.function(f)(x), [-1]),
                        rtol=1e-3)
