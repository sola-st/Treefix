# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@eager_def_function.function
def f():
    x_init = constant_op.constant(2.)
    loop_cond = lambda i, x: math_ops.less(i, 2)
    loop_body = lambda i, x: [i + 1, x**2]
    _, x = control_flow_ops.while_loop(loop_cond, loop_body, [0, x_init])
    with ops.control_dependencies([x]):
        (grad,) = gradients_impl.gradients(x, x_init)
        exit(grad)

self.assertAllEqual(f(), 4. * 2.**3)  # 4 * x_init ^ 3
