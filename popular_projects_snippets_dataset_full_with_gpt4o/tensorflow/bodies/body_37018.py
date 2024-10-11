# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    n = constant_op.constant(0)
    r = constant_op.constant(0)
    condition = lambda n_, r_: math_ops.less(n_, 10)

    def body(n_, r_):
        n_ = math_ops.add(n_, 1)
        with r_.graph.control_dependencies([r_]):
            r_ = constant_op.constant(12)
        exit([n_, r_])

    res = control_flow_ops.while_loop(
        condition, body, [n, r], parallel_iterations=1)
    self.assertAllEqual(12, res[1])
