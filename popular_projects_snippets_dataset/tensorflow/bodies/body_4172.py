# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/numpy_util_test.py
super().setUp()
global_ids = test_util.create_device_ids_array((2, 2))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: layout.Mesh([_MESH_DIM_X, _MESH_DIM_Y], global_ids, local_ids,
                        test_util.create_device_list((2, 2), device))
    for device in ('CPU', 'GPU', 'TPU')
}
self.mesh = self.configTestMesh(mesh_dict)
