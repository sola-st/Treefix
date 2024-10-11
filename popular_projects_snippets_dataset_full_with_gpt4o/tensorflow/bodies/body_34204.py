# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=None,
    max_num_elements=max_num_elements)
l = list_ops.tensor_list_push_back(l, constant_op.constant(1.0))
l = list_ops.tensor_list_push_back(l, constant_op.constant(2.0))
l = list_ops.tensor_list_push_back(l, constant_op.constant([3.0, 4.0]))

t = list_ops.tensor_list_gather(l, [1, 0], element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(t), [2.0, 1.0])

t = list_ops.tensor_list_gather(l, [2], element_dtype=dtypes.float32)
self.assertAllEqual(self.evaluate(t), [[3.0, 4.0]])

# Should raise an error when the requested tensors do not all have the same
# shape.
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Incompatible ranks during merge: 0 vs. 1"):
    t = list_ops.tensor_list_gather(l, [0, 2], element_dtype=dtypes.float32)
    self.evaluate(t)
