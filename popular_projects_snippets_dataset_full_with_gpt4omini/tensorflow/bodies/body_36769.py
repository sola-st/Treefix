# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Make sure Int writes to collections work inside of cond_v2."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        x = constant_op.constant(2)
        y = constant_op.constant(5)
        def true_fn():
            z = math_ops.add(x, y)
            ops.add_to_collection("z", 7)
            exit(math_ops.mul(x, z))

        def false_fn():
            z = math_ops.add(x, y)
            exit(math_ops.mul(x, z))

        cnd = cond_v2.cond_v2(constant_op.constant(True), true_fn, false_fn)
        self.assertEqual(self.evaluate(cnd), 14)

        read_z_collection = ops.get_collection("z")
        self.assertEqual(read_z_collection, [7])
