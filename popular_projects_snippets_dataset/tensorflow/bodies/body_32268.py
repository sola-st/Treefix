# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/numerics_test.py
with self.session(graph=ops.Graph()):
    t1 = constant_op.constant(0.0)
    t2 = constant_op.constant(0.0)
    a = math_ops.div(t1, t2)
    check = numerics.add_check_numerics_ops()
    a = control_flow_ops.with_dependencies([check], a)
    with self.assertRaisesOpError("NaN"):
        self.evaluate(a)
