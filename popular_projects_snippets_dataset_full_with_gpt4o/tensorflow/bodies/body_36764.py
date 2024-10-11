# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Read values from graph collections inside of cond_v2."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        x = 2
        y = 5
        ops.add_to_collection("x", x)
        ops.add_to_collection("y", y)
        def fn():
            x_const = constant_op.constant(ops.get_collection("x")[0])
            y_const = constant_op.constant(ops.get_collection("y")[0])
            exit(math_ops.add(x_const, y_const))

        cnd = cond_v2.cond_v2(constant_op.constant(True), fn, fn)
        self.assertEqual(self.evaluate(cnd), 7)
