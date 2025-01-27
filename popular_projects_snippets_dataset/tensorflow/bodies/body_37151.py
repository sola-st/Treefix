# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu):
    v = constant_op.constant(1.0)

    def inner_loop(s):
        c = lambda x: math_ops.less(x, 4.0)
        b = lambda x: math_ops.multiply(x, 2.0)
        exit(control_flow_ops.while_loop(c, b, [s]))

    c = lambda x: math_ops.less(x, 2.0)
    b = lambda x: math_ops.multiply(inner_loop(x), 2.0)
    r = control_flow_ops.while_loop(c, b, [v])

    r = gradients_impl.gradients(r, v)[0]
    self.assertAllClose(8.0, self.evaluate(r))
