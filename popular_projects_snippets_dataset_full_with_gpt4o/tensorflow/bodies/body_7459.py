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

self.images = stateless_random_ops.stateless_random_uniform(
    [8, 8, 3], seed=(1, 2), minval=0, maxval=255)
self.labels = stateless_random_ops.stateless_random_uniform(
    [1], seed=(1, 2), minval=0, maxval=10)

self.dataset = dataset_ops.Dataset.from_tensors(
    (self.images, self.labels)).repeat()
