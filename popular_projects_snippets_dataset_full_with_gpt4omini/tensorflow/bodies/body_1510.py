# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=[],
        max_num_elements=2)
    l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
    z = array_ops.zeros_like(l)
    z = list_ops.tensor_list_stack(z, element_dtype=dtypes.float32)
    self.assertAllEqual(z.shape.as_list(), [None])
    self.assertAllEqual(z, [0.0, 0.0])
