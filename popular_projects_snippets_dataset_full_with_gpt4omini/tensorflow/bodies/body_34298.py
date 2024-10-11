# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.cached_session():
    tensor = array_ops.placeholder(dtype=dtypes.float32)
    l = list_ops.tensor_list_split(tensor, element_shape=None, lengths=[1])
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"Tensor must be at least a vector, but saw shape: \[\]"):
        l.eval({tensor: 1})
