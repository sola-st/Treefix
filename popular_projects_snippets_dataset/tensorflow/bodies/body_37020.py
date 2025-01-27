# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    r = constant_op.constant(0)
    condition = lambda r_: math_ops.less(r_, 10)

    def body(r_):
        with r_.graph.control_dependencies([r_]):
            r_ = constant_op.constant(12)
        exit([r_])

    res = control_flow_ops.while_loop(
        condition, body, [r], parallel_iterations=1)
    self.assertAllEqual(12, self.evaluate(res))
