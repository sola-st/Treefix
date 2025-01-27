# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
super(DTensorSPMDTest, self).setUp()

self.skipForDeviceType(['TPU'],
                       'all tests require 8 TPU cores.',
                       unless_device_count_equals_to=8)

global_ids = test_util.create_device_ids_array((2, 4))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: Mesh([_MESH_DIM_X, _MESH_DIM_Y], global_ids, local_ids,
                 test_util.create_device_list((2, 4), device))
    for device in ('CPU', 'GPU', 'TPU')
}
self.mesh = self.configTestMesh(mesh_dict)

# Creates a bunch of common layouts used by tests later.
# - 0-d
self.scalar_replicated_layout = Layout.replicated(self.mesh, rank=0)
# - 1-d
self.replicated_layout_1d = Layout.replicated(self.mesh, rank=1)
self.first_dimension_sharded_layout_1d = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, rank=1)
# - 2-d
self.replicated_layout_2d = Layout.replicated(self.mesh, rank=2)
self.first_dimension_sharded_layout = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, rank=2)
self.last_dimension_sharded_layout = Layout.inner_sharded(
    self.mesh, _MESH_DIM_X, rank=2)

self.layouts_2d = [
    self.replicated_layout_2d, self.first_dimension_sharded_layout,
    self.last_dimension_sharded_layout
]

# - 3-d
self.replicated_layout_3d = Layout.replicated(self.mesh, rank=3)
self.first_dimension_sharded_layout_3d = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, rank=3)
self.middle_dimension_sharded_layout_3d = Layout(
    [layout_lib.UNSHARDED, _MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)
self.last_dimension_sharded_layout_3d = Layout.inner_sharded(
    self.mesh, _MESH_DIM_X, rank=3)

self.layouts_3d = [
    self.replicated_layout_3d, self.first_dimension_sharded_layout_3d,
    self.middle_dimension_sharded_layout_3d,
    self.last_dimension_sharded_layout_3d
]

self.shardings = {
    'batch': Layout.batch_sharded,
    'inner': Layout.inner_sharded
}
