# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r"Invalid value in lengths: -1"):
    l = list_ops.tensor_list_split([1., 2.],
                                   element_shape=None,
                                   lengths=[1, -1])
    self.evaluate(l)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Attempting to slice \[0, 3\] from tensor with length 2"):
    l = list_ops.tensor_list_split([1., 2.], element_shape=None, lengths=[3])
    self.evaluate(l)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Unused values in tensor. Length of tensor: 2 Values used: 1"):
    l = list_ops.tensor_list_split([1., 2.], element_shape=None, lengths=[1])
    self.evaluate(l)
