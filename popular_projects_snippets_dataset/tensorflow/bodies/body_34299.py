# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session():
    lengths = array_ops.placeholder(dtype=dtypes.int64)
    l = list_ops.tensor_list_split([1., 2.],
                                   element_shape=None,
                                   lengths=lengths)
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"Expected lengths to be a vector, received shape: \[\]"):
        l.eval({lengths: 1})
