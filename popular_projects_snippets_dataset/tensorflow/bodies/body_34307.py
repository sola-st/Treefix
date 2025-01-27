# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "TensorListSlice expects size to be non-negative"):
    l = list_ops.tensor_list_from_tensor([1., 2., 3.], element_shape=[])
    l = list_ops.tensor_list_resize(l, -1)
    self.evaluate(l)
