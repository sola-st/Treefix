# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session():
    t1 = list_ops.empty_tensor_list(
        element_shape=constant_op.constant([], dtype=dtypes.int32),
        element_dtype=dtypes.int32)
    i = constant_op.constant(0, dtype=dtypes.float32)
    m = constant_op.constant([1, 2, 3], dtype=dtypes.float32)

    def body(i, m, t1):
        t1 = control_flow_ops.cond(
            math_ops.equal(list_ops.tensor_list_length(t1), 0),
            lambda: list_ops.empty_tensor_list(m.shape, m.dtype), lambda: t1)

        t1 = list_ops.tensor_list_push_back(t1, m * i)
        i += 1.0
        exit((i, m, t1))

    i, m, t1 = control_flow_ops.while_loop(
        lambda i, m, t1: math_ops.less(i, 4), body, [i, m, t1])
    s1 = list_ops.tensor_list_stack(t1, element_dtype=dtypes.float32)
    np_s1 = np.vstack([np.arange(1, 4) * i for i in range(4)])
    self.assertAllEqual(self.evaluate(s1), np_s1)
