# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
super().setUp()
global_ids = test_util.create_device_ids_array((2,))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: layout.Mesh(['batch'], global_ids, local_ids,
                        test_util.create_device_list((2,), device))
    for device in ['TPU', 'GPU', 'CPU']
}
self.mesh = self.configTestMesh(mesh_dict)
