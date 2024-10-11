# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=None)
l = list_ops.tensor_list_push_back(l, [[0., 1.]])
l = list_ops.tensor_list_push_back(l, [[2.], [4.]])
with self.assertRaisesRegex(
    errors.InvalidArgumentError, r"Incompatible shapes during merge: "
    r"\[2\] vs. \[1\]"):
    t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
    self.evaluate(t)
