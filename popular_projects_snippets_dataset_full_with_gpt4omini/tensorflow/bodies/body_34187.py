# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Trying to read an uninitialized tensor but "
    "element_shape is not fully defined"):
    _, e = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    self.evaluate(e)

l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[None, 2], num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Incompatible shapes during merge: \[1,3\] vs. \[\?,2\]"):
    _, e = gen_list_ops.tensor_list_pop_back(
        l, element_dtype=dtypes.float32, element_shape=[1, 3])
    self.evaluate(e)
