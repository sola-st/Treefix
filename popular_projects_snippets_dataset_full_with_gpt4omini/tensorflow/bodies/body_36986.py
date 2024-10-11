# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    i = constant_op.constant(0)
    m = array_ops.ones([2, 2])
    c = lambda i, j: math_ops.less(i, 2)
    b = lambda i, j: [i + 1, array_ops.concat([j, j], 0)]
    with self.assertRaisesRegex(
        ValueError,
        r".*\(2, 2\).*\(4, 2\) after one iteration\. To allow the shape to "
        r"vary across iterations, use the `shape_invariants` argument of "
        r"tf.while_loop to specify a less-specific shape\."):
        control_flow_ops.while_loop(c, b, [i, m])
