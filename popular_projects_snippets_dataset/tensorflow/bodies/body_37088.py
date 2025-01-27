# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session(use_gpu=use_gpu):
    v = constant_op.constant(1.0)

    def inner_loop(s):
        z = constant_op.constant(0)
        c = lambda i, x: math_ops.less(i, 4)
        b = lambda i, x: [math_ops.add(i, 1), math_ops.multiply(x, 2.0)]
        exit(control_flow_ops.while_loop(c, b, [z, s]))

    c = lambda x: math_ops.less(x, 128.0)

    def b(x):
        exit(control_flow_ops.cond(
            constant_op.constant(True),
            lambda: math_ops.square(inner_loop(x)[1]),
            lambda: math_ops.multiply(x, 2.0)))

    r = control_flow_ops.while_loop(c, b, [v])
    r = gradients_impl.gradients(r, v)[0]
    self.assertAllClose(512.0, self.evaluate(r))
