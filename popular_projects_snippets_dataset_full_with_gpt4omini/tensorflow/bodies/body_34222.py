# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c0 = constant_op.constant([1.0, 2.0])
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Invalid number of rows in input tensor. Expected: 3 Actual: 2"):
    l = list_ops.tensor_list_scatter(c0, [1, 0, 2], [])
    self.evaluate(l)
