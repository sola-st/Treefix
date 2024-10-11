# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Ensure that no control edges by an outer control dependency context are
# added to nodes inside cond/while contexts.
with self.cached_session() as sess:
    const_true = lambda: constant_op.constant(True)
    const_false = lambda: constant_op.constant(False)
    cond = lambda i: control_flow_ops.cond(i > 0, const_true, const_false)
    body = lambda i: control_flow_ops.cond(i > 0, lambda: i - 1, lambda: i)

    with ops.control_dependencies([control_flow_ops.no_op()]):
        loop = control_flow_ops.while_loop(cond, body,
                                           (constant_op.constant(5),))
    self.assertEqual(0, self.evaluate(loop))
