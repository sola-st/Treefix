# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/add_n_test.py
with self.session(), self.test_scope():
    l1 = list_ops.tensor_list_reserve(
        element_shape=[], element_dtype=dtypes.float32, num_elements=2)
    l2 = list_ops.tensor_list_reserve(
        element_shape=[], element_dtype=dtypes.float32, num_elements=3)
    l = math_ops.add_n([l1, l2])
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "TensorList arguments to AddN must all have the same shape"):
        list_ops.tensor_list_stack(l, element_dtype=dtypes.float32).eval()
