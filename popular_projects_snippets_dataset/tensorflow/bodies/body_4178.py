# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/numpy_util_test.py
t00 = np.array([[0, 1], [4, 5]])
t01 = np.array([[2, 3], [6, 7]])
t10 = np.array([[8, 9], [12, 13]])
t11 = np.array([[10, 11], [14, 15]])
tensors = [t00, t01, t10, t11]
sharded_on_x_y = layout.Layout([_MESH_DIM_X, _MESH_DIM_Y], mesh=self.mesh)
self.assertAllClose(
    numpy_util.unpacked_to_numpy(tensors, sharded_on_x_y),
    np.arange(16).reshape(4, 4))
