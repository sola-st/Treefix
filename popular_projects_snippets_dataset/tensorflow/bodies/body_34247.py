# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session():
    tl = list_ops.empty_tensor_list(
        element_shape=constant_op.constant([1], dtype=dtypes.int32),
        element_dtype=dtypes.int32)
    tl = list_ops.tensor_list_push_back(tl, [1])
    self.assertAllEqual(
        self.evaluate(
            list_ops.tensor_list_stack(tl, element_dtype=dtypes.int32)),
        [[1]])
