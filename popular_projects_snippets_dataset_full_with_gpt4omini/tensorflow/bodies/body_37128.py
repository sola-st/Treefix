# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
var = resource_variable_ops.ResourceVariable(constant_op.constant(3.0))

@eager_def_function.function
def test_fn():
    x = constant_op.constant(0.0)
    r = control_flow_ops.while_loop(
        # Outer loop condition
        lambda i, y: i < 2,
        # Outer loop body
        lambda i, y: (i + 1, y + control_flow_ops.cond(
            constant_op.constant(True),
            # True branch
            lambda: control_flow_ops.while_loop(
                # Inner loop condition
                lambda j, z: j < 3,
                # Inner loop body
                lambda j, z: (j + 1, z + math_ops.square(var)),
                # Inner initial loop value
                [0, y])[1],
            # False branch
            lambda: (0.0))),
        # Outer initial loop value
        [0, x])[1]

    grad = gradients_impl.gradients(r, x)[0]
    exit((r, grad))

self.evaluate(variables.global_variables_initializer())
r, grad = self.evaluate(test_fn())
# 2 * 3 * 3^2
self.assertEqual(r, 81.0)
# v1 control flow gets the wrong answer!!!
# Gradient computation:
#   f(x) = x + 3^2
#   inner_loop(x) = f(f(f(x))) = x + 3*3^2 = x + 27
#   g(x) = x + inner_loop(x) = 2x + 27
#   outer_loop(x) = g(g(x)) = 4x + 81
#   outer_loop'(x) = 4
# Note that v1 control flow gets 4.0 as well if the cond is removed.
if control_flow_util.ENABLE_CONTROL_FLOW_V2:
    self.assertEqual(grad, 4.0)
