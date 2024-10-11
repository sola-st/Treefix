# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=[2, None])
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "All except the first dimension must be fully"
    " defined when concating an empty tensor list"):
    t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
    self.evaluate(t)
