# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session():
    list_ = list_ops.empty_tensor_list(
        element_shape=constant_op.constant([], dtype=dtypes.int32),
        element_dtype=dtypes.int32)
    m = constant_op.constant([1, 2, 3], dtype=dtypes.float32)

    def body(list_, m):
        list_ = control_flow_ops.cond(
            math_ops.equal(list_ops.tensor_list_length(list_), 0),
            lambda: list_ops.empty_tensor_list(m.shape, m.dtype), lambda: list_)
        list_ = list_ops.tensor_list_push_back(list_, m)
        exit((list_, m))

    for _ in range(2):
        list_, m = body(list_, m)

    s1 = list_ops.tensor_list_stack(list_, element_dtype=dtypes.float32)
    np_s1 = np.array([[1, 2, 3], [1, 2, 3]], dtype=np.float32)
    self.assertAllEqual(self.evaluate(s1), np_s1)
