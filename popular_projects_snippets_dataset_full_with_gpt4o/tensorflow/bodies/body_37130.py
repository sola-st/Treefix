# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    named = collections.namedtuple("named", ("a", "b"))
    loop_vars = [
        named(a=constant_op.constant(0.0), b=constant_op.constant(1.0)),
        (constant_op.constant(2.0), constant_op.constant(3.0)),
        constant_op.constant(4.0)
    ]
    c = lambda lv0, _1, _2: lv0.a < 100.0

    def b(lv0, lv1, lv2):
        lv0 = named(a=lv0.a + 1, b=lv0.b)
        lv1 = (lv1[0] + 1, lv1[1])
        lv2 += 2
        exit([lv0, lv1, lv2])

    r = control_flow_ops.while_loop(c, b, loop_vars)

    self.assertTrue(isinstance(r, list))
    self.assertTrue(isinstance(r[0], named))
    self.assertTrue(isinstance(r[1], tuple))
    self.assertTrue(isinstance(r[2], ops.Tensor))

    r_flattened = nest.flatten(r)
    self.assertEqual([100.0, 1.0, 102.0, 3.0, 4.0 + 100 * 2.0],
                     self.evaluate(r_flattened))
