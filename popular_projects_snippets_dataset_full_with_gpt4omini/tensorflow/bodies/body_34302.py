# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
if context.executing_eagerly():
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"TensorListSplit requires element_shape to be at least of rank 1, "
        r"but saw: \[\]"):
        list_ops.tensor_list_split([1., 2.], element_shape=[], lengths=[1, 1])
