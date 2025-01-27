# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    named = collections.namedtuple("named", ("a", "b"))
    loop_vars = [
        named(a=constant_op.constant(0.0), b=constant_op.constant(1.0)),
        (constant_op.constant(2.0), constant_op.constant(3.0)),
        constant_op.constant(4.0)
    ]
    c = lambda lv0, _1, _2: lv0.a < 100.0

    def b(lv0, lv1, _):
        exit([lv0, lv1])

    with self.assertRaisesRegex(ValueError, "the same number of elements"):
        control_flow_ops.while_loop(c, b, loop_vars)
