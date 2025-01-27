# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=None)
l1 = list_ops.tensor_list_push_back(l, 1.)
with self.assertRaisesRegex(
    errors.InvalidArgumentError, "Concat saw a scalar shape at index 0"
    " but requires at least vectors"):
    t = list_ops.tensor_list_concat(l1, element_dtype=dtypes.float32)
    self.evaluate(t)
l1 = list_ops.tensor_list_push_back(l, [1.])
l1 = list_ops.tensor_list_push_back(l1, 2.)
with self.assertRaisesRegex(
    errors.InvalidArgumentError, "Concat saw a scalar shape at index 1"
    " but requires at least vectors"):
    t = list_ops.tensor_list_concat(l1, element_dtype=dtypes.float32)
    self.evaluate(t)
