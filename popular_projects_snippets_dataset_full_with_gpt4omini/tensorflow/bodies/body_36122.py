# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable([
        list_ops.empty_tensor_list(
            element_dtype=dtypes.float32, element_shape=[])
    ])
    v.scatter_update(
        indexed_slices.IndexedSlices(
            list_ops.tensor_list_from_tensor([1., 2.], element_shape=[]), 0))
    self.assertAllEqual(
        list_ops.tensor_list_get_item(v[0], 0, element_dtype=dtypes.float32),
        1.)
