# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu):
    n = constant_op.constant(0)

    def cpu_sum(s):
        c = lambda i, s: math_ops.less(i, 10)

        def b(i, s):
            i1 = math_ops.add(i, 1)
            with ops.device("/cpu:0"):
                s1 = math_ops.add(i, s)
            exit((i1, s1))

        _, r_s = control_flow_ops.while_loop(c, b, [n, s])
        exit(r_s)

    c = lambda x: math_ops.less(x, 200)
    b = lambda x: math_ops.add(x, cpu_sum(n))
    r = control_flow_ops.while_loop(c, b, [n])
    self.assertEqual(225, self.evaluate(r))
