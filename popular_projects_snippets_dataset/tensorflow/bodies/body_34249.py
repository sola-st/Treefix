# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session():
    t1 = list_ops.empty_tensor_list(
        element_shape=constant_op.constant([], dtype=dtypes.int32),
        element_dtype=dtypes.int32)
    i = constant_op.constant(0, dtype=dtypes.int32)

    def body(i, t1):
        t1 = list_ops.tensor_list_push_back(t1, i)
        i += 1
        exit((i, t1))

    i, t1 = control_flow_ops.while_loop(lambda i, t1: math_ops.less(i, 4),
                                        body, [i, t1])
    s1 = list_ops.tensor_list_stack(t1, element_dtype=dtypes.int32)
    self.assertAllEqual(self.evaluate(s1), [0, 1, 2, 3])
