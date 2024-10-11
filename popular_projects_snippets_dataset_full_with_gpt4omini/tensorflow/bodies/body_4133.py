# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
params = np.arange(1000 * 4).reshape((1000, 4)).astype(np.float32)
# "batch" size = 2, num_indices = 4 per example
indices = np.random.randint(
    0, 1000, size=4 * 4).reshape((4, 4)).astype(np.int32)
expected = array_ops.gather_v2(params, indices, axis=0)

params = numpy_util.pack_numpy(
    params, layout=Layout([_MESH_DIM_X, layout_lib.UNSHARDED], self.mesh))
indices = numpy_util.pack_numpy(
    indices, Layout([layout_lib.UNSHARDED, layout_lib.UNSHARDED],
                    self.mesh))

expected_layout = Layout(
    [layout_lib.UNSHARDED, layout_lib.UNSHARDED, layout_lib.UNSHARDED],
    self.mesh)
with api.run_on(self.mesh):
    dtensor_result = array_ops.gather_v2(params, indices, axis=0)
    self.assertDTensorEqual(expected, expected_layout, dtensor_result)
