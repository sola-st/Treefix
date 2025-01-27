# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['CPU', 'GPU'], 'Testing only for TPU.')

global_ids = test_util.create_device_ids_array((2, 4))
local_ids = np.ravel(global_ids).tolist()

tpu_mesh = Mesh([_MESH_DIM_X, _MESH_DIM_Y], global_ids, local_ids,
                test_util.create_device_list((2, 4), 'TPU'))
cpu_mesh = Mesh([_MESH_DIM_X, _MESH_DIM_Y], global_ids, local_ids,
                test_util.create_device_list((2, 4), 'CPU'))

cpu_layout = Layout.replicated(cpu_mesh, rank=4)
if shard_spec == 'sharded':
    tpu_layout = Layout.batch_sharded(tpu_mesh, _MESH_DIM_X, rank=4)
else:
    tpu_layout = Layout.replicated(tpu_mesh, rank=4)

inputs = stateless_random_ops.stateless_random_uniform(
    shape=(8, 9, 9, 1), seed=[0, 1])
expected_result = gen_string_ops.string_format(inputs=[inputs])

inputs = numpy_util.pack_numpy(inputs, tpu_layout)
# StringFormat is not supported on TPU, so copy_to_mesh to the CPU.
# Since we cannot eager copy_to_mesh from an input with non-replicated
# layout yet, relayout to replicated layout first, and then transfer to CPU.
inputs = api.copy_to_mesh(
    api.relayout(inputs, Layout.replicated(tpu_mesh, rank=4)), cpu_layout)

got = gen_string_ops.string_format(inputs=[inputs])
# Manually compare instead of assertDTensorEqual since outputs are strings.
self.assertEqual(api.fetch_layout(got), Layout.replicated(cpu_mesh, rank=0))
for got_tensor in api.unpack(got):
    self.assertEqual(expected_result, got_tensor)
