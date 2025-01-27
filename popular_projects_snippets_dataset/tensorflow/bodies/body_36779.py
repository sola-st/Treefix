# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default() as g:
    with self.session(graph=g):

        a = constant_op.constant([2.0], name="a")
        b = constant_op.constant([2.0], name="b")

        def fn2():
            with ops.colocate_with(b.op):
                c = constant_op.constant(3.0)
                self.assertEqual([b"loc:@a", b"loc:@b"], c.op.colocation_groups())
                exit(c)

        with ops.colocate_with(a.op):
            self.assertEqual(
                cond_v2.cond_v2(constant_op.constant(True), fn2, fn2).eval(), 3)

            d = constant_op.constant([2.0], name="d")
            self.assertEqual([b"loc:@a"], d.op.colocation_groups())
