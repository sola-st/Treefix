# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
# Should be able to gather from empty lists with fully defined
# element_shape.
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=[1, 2],
    max_num_elements=max_num_elements)
t = list_ops.tensor_list_gather(l, [], element_dtype=dtypes.float32)
self.assertAllEqual((0, 1, 2), self.evaluate(t).shape)

# Should not be able to gather from empty lists with partially defined
# element_shape.
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "non-fully-defined"):
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=[None, 2],
        max_num_elements=max_num_elements)
    t = list_ops.tensor_list_gather(l, [], element_dtype=dtypes.float32)
    self.evaluate(t)

# Should not be able to gather from empty lists with undefined
# element_shape.
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "non-fully-defined"):
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=None,
        max_num_elements=max_num_elements)
    t = list_ops.tensor_list_gather(l, [], element_dtype=dtypes.float32)
    self.evaluate(t)
