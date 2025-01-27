# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
has_enable_dtensor_mixed_precision_reduce = (
    'DTENSOR_ENABLE_MIXED_PRECISION_REDUCE' in os.environ
)
has_dtensor_reduce_in_bfloat16_max_group_size = (
    'DTENSOR_REDUCE_IN_BFLOAT16_MAX_GROUP_SIZE' in os.environ
)
if has_dtensor_reduce_in_bfloat16_max_group_size:
    old_dtensor_reduce_in_bfloat16_max_group_size = os.environ[
        'DTENSOR_REDUCE_IN_BFLOAT16_MAX_GROUP_SIZE']
os.environ['DTENSOR_ENABLE_MIXED_PRECISION_REDUCE'] = ''
os.environ['DTENSOR_REDUCE_IN_BFLOAT16_MAX_GROUP_SIZE'] = '4'

self.skipForDeviceType(['GPU'],
                       'GPUs do not support bfloat16 reduce')
self.skipForDeviceType(['TPU'],
                       'This test requires 8 TPU cores.',
                       unless_device_count_equals_to=8)

# Create and use an 8-device mesh just for this test. Mixed-precision
# AllReduce will be in effect since the reduction will be across 8 devices
# which is larger than the max group size flag value of 4.
global_ids = test_util.create_device_ids_array((8,))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: layout_lib.Mesh([_MESH_DIM_X], global_ids, local_ids,
                            test_util.create_device_list((8,), device))
    for device in ('CPU', 'GPU', 'TPU')
}

mesh = self.configTestMesh(mesh_dict)
replicated_layout_1d = Layout.replicated(mesh, rank=1)
first_dim_sharded_layout_1d = Layout.batch_sharded(
    mesh, _MESH_DIM_X, rank=2)

@polymorphic_function.function
def func(x):
    exit(math_ops.reduce_sum(x, axis=0))

# Reduce across 8 devices.
inp = constant_op.constant(
    np.arange(48.).reshape((8, 6)), dtype=dtypes.bfloat16)
expected_result = np.sum(inp, axis=0)

inp_dtensor = numpy_util.pack_numpy(inp, first_dim_sharded_layout_1d)
dtensor_result = func(inp_dtensor)

self.assertDTensorEqual(
    expected_result, replicated_layout_1d, dtensor_result)

if not has_enable_dtensor_mixed_precision_reduce:
    del os.environ['DTENSOR_ENABLE_MIXED_PRECISION_REDUCE']
if has_dtensor_reduce_in_bfloat16_max_group_size:
    os.environ['DTENSOR_REDUCE_IN_BFLOAT16_MAX_GROUP_SIZE'] = (
        old_dtensor_reduce_in_bfloat16_max_group_size
    )
else:
    del os.environ['DTENSOR_REDUCE_IN_BFLOAT16_MAX_GROUP_SIZE']
