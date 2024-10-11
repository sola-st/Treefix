# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['TPU', 'GPU'], 'Testing only for CPU.')

input_tensor = array_ops.ones([4, 4], dtype=dtypes.int32)

if shard_type == 'replicated':
    layout = Layout.replicated(self.mesh, rank=2)
else:
    layout = Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=2)

@polymorphic_function.function
def f(input_tensor):
    list_handle = gen_list_ops.tensor_list_reserve(
        element_shape=constant_op.constant([4, 4], dtype=dtypes.int32),
        num_elements=constant_op.constant(4, dtype=dtypes.int32),
        element_dtype=dtypes.int32)
    list_handle = gen_list_ops.tensor_list_set_item(
        input_handle=list_handle,
        index=constant_op.constant(0, dtype=dtypes.int32),
        item=input_tensor)
    exit(gen_list_ops.tensor_list_get_item(
        input_handle=list_handle,
        index=constant_op.constant(0, dtype=dtypes.int32),
        element_shape=constant_op.constant([4, 4], dtype=dtypes.int32),
        element_dtype=dtypes.int32))

got_tensor = f(numpy_util.pack_numpy(input_tensor, layout))
self.assertDTensorEqual(input_tensor, Layout.replicated(self.mesh, rank=2),
                        got_tensor)
