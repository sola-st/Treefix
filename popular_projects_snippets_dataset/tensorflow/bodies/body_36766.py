# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Read tensors from collections inside of cond_v2 & use them."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        x = constant_op.constant(2)
        y = constant_op.constant(5)
        ops.add_to_collection("x", x)
        ops.add_to_collection("y", y)

        def fn():
            x_read = ops.get_collection("x")[0]
            y_read = ops.get_collection("y")[0]
            exit(math_ops.add(x_read, y_read))

        cnd = cond_v2.cond_v2(math_ops.less(x, y), fn, fn)
        self.assertEqual(self.evaluate(cnd), 7)
