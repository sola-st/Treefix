# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c = constant_op.constant([1.0, 2.0], dtype=dtypes.float32)
l0 = list_ops.tensor_list_from_tensor(c, element_shape=[])
l1 = list_ops.tensor_list_from_tensor([-1.0], element_shape=[])
l_batch = array_ops.stack([l0, l1])
l_push = list_ops.tensor_list_push_back_batch(l_batch, [3.0, 4.0])
l_unstack = array_ops.unstack(l_push)
l0_ret = list_ops.tensor_list_stack(l_unstack[0], dtypes.float32)
l1_ret = list_ops.tensor_list_stack(l_unstack[1], dtypes.float32)
self.assertAllClose([1.0, 2.0, 3.0], self.evaluate(l0_ret))
self.assertAllClose([-1.0, 4.0], self.evaluate(l1_ret))

with ops.control_dependencies([l_push]):
    l_unstack_orig = array_ops.unstack(l_batch)
    l0_orig_ret = list_ops.tensor_list_stack(l_unstack_orig[0],
                                             dtypes.float32)
    l1_orig_ret = list_ops.tensor_list_stack(l_unstack_orig[1],
                                             dtypes.float32)

# Check that without aliasing, push_back_batch still works; and
# that it doesn't modify the input.
l0_r_v, l1_r_v, l0_orig_v, l1_orig_v = self.evaluate(
    (l0_ret, l1_ret, l0_orig_ret, l1_orig_ret))
self.assertAllClose([1.0, 2.0, 3.0], l0_r_v)
self.assertAllClose([-1.0, 4.0], l1_r_v)
self.assertAllClose([1.0, 2.0], l0_orig_v)
self.assertAllClose([-1.0], l1_orig_v)

# Pushing back mismatched shapes fails.
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    self.evaluate(list_ops.tensor_list_push_back_batch(l_batch, []))

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "incompatible shape to a list at index 0"):
    self.evaluate(
        list_ops.tensor_list_push_back_batch(l_batch, [[3.0], [4.0]]))

if context.executing_eagerly():
    expected_error = (errors.InvalidArgumentError, "Invalid data type")
else:
    expected_error = (ValueError, "wrong element dtype")
with self.assertRaisesRegex(*expected_error):
    self.evaluate(list_ops.tensor_list_push_back_batch(l_batch, [3, 4]))
