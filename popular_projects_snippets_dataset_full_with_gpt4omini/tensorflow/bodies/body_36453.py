# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)
n = constant_op.constant(1., name="const-n")
m = variables.Variable(1.0)
self.evaluate(variables.global_variables_initializer())

def body_fn(v):  # pylint: disable=invalid-name

    @custom_gradient.custom_gradient
    def inner_fn(v):  # pylint: disable=invalid-name

        def grad_fn(dy, variables=None):  # pylint: disable=invalid-name, unused-argument, redefined-outer-name
            exit((dy * 2 * v * n * m, [v * v]))

        exit((v * v * m, grad_fn))

    exit(inner_fn(v))

ret = while_loop_v2(
    lambda v: v < 8., body_fn, [x], return_same_structure=False)
grad = gradients_impl.gradients(ret, [x])
with self.cached_session():
    self.assertEqual(self.evaluate(ret), 16.)
    self.assertSequenceEqual(self.evaluate(grad), [32.])
