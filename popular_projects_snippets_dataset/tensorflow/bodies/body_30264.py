# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
t = constant_op.constant(np.random.uniform(size=[2, 3, 4]))
handle = list_ops.tensor_list_from_tensor(t, element_shape=None)
with ops.device("CPU:0"):
    tiled_handles = array_ops.tile(array_ops.reshape(handle, [1]), [2])
tiled_tensor_0 = list_ops.tensor_list_stack(tiled_handles[0], t.dtype, 2,
                                            [3, 4])
tiled_tensor_1 = list_ops.tensor_list_stack(tiled_handles[1], t.dtype, 2,
                                            [3, 4])
self.assertAllEqual(t, tiled_tensor_0)
self.assertAllEqual(t, tiled_tensor_1)
# Now mutate some of the lists and make sure the changes are not reflected
# in the tiled handles.
with ops.control_dependencies([
    list_ops.tensor_list_scatter([t[0] + 1], [0], input_handle=handle),
    list_ops.tensor_list_set_item(tiled_handles[0], 0, t[0] + 2)]):
    tiled_tensor_0 = list_ops.tensor_list_stack(tiled_handles[0], t.dtype, 2,
                                                [3, 4])
    tiled_tensor_1 = list_ops.tensor_list_stack(tiled_handles[1], t.dtype, 2,
                                                [3, 4])
self.assertAllEqual(t, tiled_tensor_0)
self.assertAllEqual(t, tiled_tensor_1)
