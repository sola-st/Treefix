# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    alive = constant_op.constant(True, name="alive")
    count = constant_op.constant(0, name="count")

    def body(i):
        exit(control_flow_ops.cond(
            alive, lambda: [math_ops.less(i, 3), math_ops.add(count, 1)],
            lambda: [alive, count]))

    for i in range(10):
        alive, count = body(i)
    self.assertAllEqual(4, self.evaluate(count))
