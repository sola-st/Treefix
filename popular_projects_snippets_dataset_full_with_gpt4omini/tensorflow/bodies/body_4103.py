# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
super(DTensorLayoutPropSPMDTest, self).setUp()

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

self.scalar_replicated_layout = Layout.replicated(self.mesh, rank=0)

self.replicated_layout_1d = Layout.replicated(self.mesh, rank=1)
self.first_dimension_sharded_layout_1d = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, rank=1)

self.replicated_layout_2d = Layout.replicated(self.mesh, rank=2)
self.first_dimension_sharded_layout_2d = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, rank=2)
self.last_dimension_sharded_layout_2d = Layout.inner_sharded(
    self.mesh, _MESH_DIM_X, rank=2)

self.replicated_layout_3d = Layout.replicated(self.mesh, rank=3)
self.first_dimension_sharded_layout_3d = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, rank=3)
self.middle_dimension_sharded_layout_3d = Layout(
    [layout_lib.UNSHARDED, _MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)
self.last_dimension_sharded_layout_3d = Layout.inner_sharded(
    self.mesh, _MESH_DIM_X, rank=3)

# Make a list so that we can index layouts by sharding dimension and then
# by rank.
self.layouts = [
    [
        None, self.first_dimension_sharded_layout_1d,
        self.first_dimension_sharded_layout_2d,
        self.first_dimension_sharded_layout_3d
    ],
    [
        None, None, self.last_dimension_sharded_layout_2d,
        self.middle_dimension_sharded_layout_3d
    ],
    [None, None, None, self.last_dimension_sharded_layout_3d],
    # Keep this at the end so a sharding dim of -1 corresponds to
    # replicated.
    [
        None, self.replicated_layout_1d, self.replicated_layout_2d,
        self.replicated_layout_3d
    ],
]
