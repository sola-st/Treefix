# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/numpy_util_test.py
t00 = np.arange(8).reshape(2, 4)
t01 = np.arange(8, 16).reshape(2, 4)
t10 = np.arange(8).reshape(2, 4)
t11 = np.arange(8, 16).reshape(2, 4)
tensors = [t00, t01, t10, t11]
sharded_on_y = layout.Layout([_MESH_DIM_Y, layout.UNSHARDED],
                             mesh=self.mesh)
self.assertAllClose(
    numpy_util.unpacked_to_numpy(tensors, sharded_on_y),
    np.arange(16).reshape(4, 4))
