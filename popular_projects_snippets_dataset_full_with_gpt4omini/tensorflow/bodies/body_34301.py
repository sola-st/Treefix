# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.assertRaisesRegex(ValueError,
                            r"Shapes must be equal rank, but are 1 and 0"):
    l = list_ops.tensor_list_split([1., 2.], element_shape=[], lengths=[1, 1])
with self.cached_session():
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"TensorListSplit requires element_shape to be at least of rank 1, "
        r"but saw: \[\]"):
        element_shape = array_ops.placeholder(dtype=dtypes.int32)
        l = list_ops.tensor_list_split([1., 2.],
                                       element_shape=element_shape,
                                       lengths=[1, 1])
        l.eval({element_shape: []})
