# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    l = list_ops.empty_tensor_list(
        element_shape=[], element_dtype=dtypes.float32, max_num_elements=2)
    # SetItem should not change the push index.
    l = list_ops.tensor_list_set_item(l, 1, 3.)
    l = list_ops.tensor_list_push_back(l, 5.)
    l = list_ops.tensor_list_push_back(l, 7.)
    t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
    self.assertAllEqual(t, [5., 7.])
