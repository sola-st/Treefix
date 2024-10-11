# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c = constant_op.constant([1.0, 2.0])
l = list_ops.tensor_list_from_tensor(c, element_shape=[])
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(list_ops.tensor_list_set_item(l, 20, 3.0))
