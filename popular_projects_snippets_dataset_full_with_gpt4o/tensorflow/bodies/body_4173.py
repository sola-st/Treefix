# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/numpy_util_test.py
tensors = [np.arange(4) for i in range(self.mesh.size)]
replicated_layout = layout.Layout([layout.UNSHARDED, layout.UNSHARDED],
                                  mesh=self.mesh)

self.assertAllClose(
    np.arange(4), numpy_util.unpacked_to_numpy(tensors, replicated_layout))
