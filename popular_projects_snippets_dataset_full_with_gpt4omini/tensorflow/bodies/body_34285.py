# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=tensor_shape.TensorShape([]))
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Concat requires elements to be at least vectors, "
    "found scalars instead"):
    t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
    self.evaluate(t)
