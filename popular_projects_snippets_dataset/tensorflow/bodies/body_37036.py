# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu) as sess:
    p = array_ops.placeholder(dtypes.bool)
    n = constant_op.constant(0.0)

    def c(x):
        exit(math_ops.less(x, 10.0))

    def b(x):
        with ops.device("/cpu:0"):
            x1 = math_ops.add(x, 1.0)
        exit(x1)

    r = control_flow_ops.cond(p,
                              lambda: control_flow_ops.while_loop(c, b, [n]),
                              lambda: math_ops.multiply(n, 2.0))
    r1 = gradients_impl.gradients(r, [n])
    self.assertEqual(10., sess.run(r, {p: True}))
    self.assertEqual([1.0], sess.run(r1, {p: True}))
    self.assertEqual(0.0, sess.run(r, {p: False}))
    self.assertEqual([2.0], sess.run(r1, {p: False}))
