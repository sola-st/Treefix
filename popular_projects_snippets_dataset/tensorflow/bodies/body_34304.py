# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
if context.executing_eagerly():
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"tensor shape \[2,1\] is not compatible with element_shape \[1\]"):
        list_ops.tensor_list_split([[1.], [2.]],
                                   element_shape=[1],
                                   lengths=[1, 1])
