# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    l = list_ops.tensor_list_reserve(
        element_dtype=dtypes.float32, element_shape=None, num_elements=2)
    l = list_ops.tensor_list_set_item(l, 0, [3.0, 4.0])
    t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
    self.assertAllEqual(t, [[3.0, 4.0], [0., 0.]])
