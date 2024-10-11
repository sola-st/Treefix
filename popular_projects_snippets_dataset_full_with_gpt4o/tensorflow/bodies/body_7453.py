# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
super().setUp()
global_ids = test_util.create_device_ids_array((2, 1))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: layout.Mesh(['batch', 'model'], global_ids, local_ids,
                        test_util.create_device_list((2,), device))
    for device in ['TPU', 'GPU', 'CPU']
}
self.mesh_2d = self.configTestMesh(mesh_dict)
