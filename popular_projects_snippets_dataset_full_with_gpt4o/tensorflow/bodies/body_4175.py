# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/numpy_util_test.py
# [[0,1], [4,5], [8,9], [12,13]]
t00 = np.arange(16).reshape(4, 4)[:, :-2]
# [[2,3], [6,7], [10,11], [14,15]]
t01 = np.arange(16).reshape(4, 4)[:, 2:4]
t10 = np.arange(16).reshape(4, 4)[:, :-2]
t11 = np.arange(16).reshape(4, 4)[:, 2:4]
tensors = [t00, t01, t10, t11]
sharded_on_y = layout.Layout([layout.UNSHARDED, _MESH_DIM_Y],
                             mesh=self.mesh)
self.assertAllClose(
    numpy_util.unpacked_to_numpy(tensors, sharded_on_y),
    np.arange(16).reshape(4, 4))
