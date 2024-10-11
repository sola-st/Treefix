# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    i = constant_op.constant(0)
    m = array_ops.ones([2, 2])
    c = lambda i, j: math_ops.less(i, 2)

    def _b(i, j):
        new_i = math_ops.add(i, 1)
        new_j = array_ops.tile(j, [2, 2])
        exit([new_i, new_j])

    r = control_flow_ops.while_loop(
        c, _b, [i, m],
        [i.get_shape(), tensor_shape.unknown_shape()])
    r = r[1] * array_ops.ones([8, 8])
    self.assertAllEqual(np.ones((8, 8)), self.evaluate(r))
