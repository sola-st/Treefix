# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
if axis != -1:
    self.skipTest('b/177569789: fix this test with layout propagation v2')

indices = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.int32)
depth = constant_op.constant(10, dtype=dtypes.int32)
indices_layout = (
    self.replicated_layout_2d
    if shard_type == 'replicated' else self.first_dimension_sharded_layout)
output_layout = (
    Layout.replicated(self.mesh, rank=3) if shard_type == 'replicated' else
    Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=3))

expected_result = array_ops.one_hot(indices, depth, axis=axis)

indices = numpy_util.pack_numpy(indices, indices_layout)
depth = api.copy_to_mesh(depth, self.scalar_replicated_layout)
dtensor_result = array_ops.one_hot(indices, depth, axis=axis)
if axis == 0 and shard_type == 'batch_sharded':
    output_layout = self.middle_dimension_sharded_layout_3d

self.assertDTensorEqual(expected_result, output_layout, dtensor_result)
