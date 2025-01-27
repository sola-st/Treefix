# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=[], max_num_elements=1)
l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Tried to push item into a full list"):
    l = list_ops.tensor_list_push_back(l, 2.)
    self.evaluate(l)
