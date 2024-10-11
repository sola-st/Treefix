# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    q = data_flow_ops.FIFOQueue(-1, dtypes.int32)
    i = constant_op.constant(0)

    def c(i):
        exit(math_ops.less(i, 10))

    def b(i):
        ni = math_ops.add(i, 1)
        ni = control_flow_ops.with_dependencies([q.enqueue((i,))], ni)
        exit(ni)

    r = control_flow_ops.while_loop(c, b, [i], parallel_iterations=1)
    self.assertEqual([10], self.evaluate(r))
    for i in range(10):
        self.assertEqual([i], self.evaluate(q.dequeue()))
