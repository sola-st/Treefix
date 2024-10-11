# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=[],
    max_num_elements=max_num_elements)
l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
l = list_ops.tensor_list_push_back(l, constant_op.constant(2.0))
t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
if not context.executing_eagerly():
    self.assertAllEqual(t.shape.as_list(), [None])
self.assertAllEqual(self.evaluate(t), [1.0, 2.0])
