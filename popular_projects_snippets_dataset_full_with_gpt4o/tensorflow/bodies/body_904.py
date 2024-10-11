# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/add_n_test.py
with self.session(), self.test_scope():
    l1 = list_ops.tensor_list_reserve(
        element_shape=[], element_dtype=dtypes.float32, num_elements=3)
    l2 = list_ops.tensor_list_reserve(
        element_shape=[], element_dtype=dtypes.float32, num_elements=3)
    l1 = list_ops.tensor_list_set_item(l1, 0, 5.)
    l2 = list_ops.tensor_list_set_item(l2, 2, 10.)

    l = math_ops.add_n([l1, l2])
    self.assertAllEqual(
        list_ops.tensor_list_stack(l, element_dtype=dtypes.float32),
        [5.0, 0.0, 10.0])
