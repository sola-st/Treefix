# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
super(CollectiveTest, self).setUp()

global_ids = test_util.create_device_ids_array((2, 1))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: layout_lib.Mesh(_MESH_DIMS, global_ids, local_ids,
                            test_util.create_device_list((2, 1), device))
    for device in ('CPU', 'GPU', 'TPU')
}
self.mesh = self.configTestMesh(mesh_dict)
self.fully_replicated_layout_2d = Layout.replicated(self.mesh, rank=2)
self.first_dimension_sharded_layout_2d = Layout.batch_sharded(
    self.mesh, _MESH_DIM_X, 2)
self.scalar_layout = Layout.replicated(self.mesh, rank=0)
