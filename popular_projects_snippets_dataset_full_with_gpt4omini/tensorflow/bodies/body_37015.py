# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Test the cases that A -> Enter and Exit -> A are partitioned.
with self.cached_session(use_gpu=use_gpu):
    s0 = constant_op.constant(2.0)

    def inner_loop(s):
        c = lambda s: math_ops.less(s, 20.0)

        def b(s):
            s1 = math_ops.add(s, s)
            exit(s1)

        r_s = control_flow_ops.while_loop(c, b, [s], parallel_iterations=1)
        exit(r_s)

    outer_c = lambda x: math_ops.less(x, 3000.0)

    def outer_b(x):
        x = logging_ops.Print(x, [x])  # Edge "Print -> Enter" is partitioned
        x = inner_loop(x)
        with ops.device("/cpu:0"):
            x = math_ops.square(x)  # Edge "Exit -> Square" is partitioned
        exit(x)

    r = control_flow_ops.while_loop(
        outer_c, outer_b, [s0], parallel_iterations=1)
    self.assertEqual(1048576.0, self.evaluate(r))
