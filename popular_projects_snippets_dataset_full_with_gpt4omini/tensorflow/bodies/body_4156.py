# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
super(DTensorRelayoutTest, self).setUp()

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
context.ensure_initialized()
