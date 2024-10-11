# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c0 = constant_op.constant([1.0, 2.0])
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Indices in TensorListScatter must all be non-negative."):
    l = list_ops.tensor_list_scatter(c0, [-1, -2], element_shape=[])
    self.evaluate(l)
