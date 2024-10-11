# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
super(DTensorConvSPMDTest, self).setUp()

# TODO(b/169436213): Re-enable TPU after figuring out multi-chip story.
self.skipForDeviceType(['TPU'], 'reserving 4 chips on forge is unreliable')

if config.list_physical_devices('GPU') or config.list_logical_devices(
    'TPU_SYSTEM'):
    self.skipTest(
        'Skipping as 3D mesh with 18 devices cannot be tested on GPU/TPU.')

# Builds a 2x3x3 mesh.
self._mesh_dim_b = 'b'
self._mesh_dim_x = 'x'
self._mesh_dim_y = 'y'
self._dims = [self._mesh_dim_b, self._mesh_dim_x, self._mesh_dim_y]

global_ids = test_util.create_device_ids_array([2, 3, 3])
local_ids = np.ravel(global_ids).tolist()

mesh_dict = {
    device: Mesh(self._dims, global_ids, local_ids,
                 test_util.create_device_list([2, 3, 3], 'CPU'))
    for device in ('CPU', 'GPU', 'TPU')
}
self.mesh = self.configTestMesh(mesh_dict)
self._num_devices = self.mesh.size
test_util.reset_logical_devices('CPU', self.mesh.size)
