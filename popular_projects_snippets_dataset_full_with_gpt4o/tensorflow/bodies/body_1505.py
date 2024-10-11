# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32, element_shape=None, max_num_elements=2)
    l = list_ops.tensor_list_push_back(l, [3.0, 4.0])
    # Pushing an element with a different shape should raise an error.
    with self.assertRaisesRegex(errors.InternalError, "shape"):
        l = list_ops.tensor_list_push_back(l, 5.)
        self.evaluate(
            list_ops.tensor_list_stack(l, element_dtype=dtypes.float32))
