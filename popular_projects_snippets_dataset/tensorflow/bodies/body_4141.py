# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
params = np.arange(128 * 1000 * 2).reshape(
    (128, 1000, 2)).astype(np.float32)
indices = np.random.randint(
    0, 1000, size=128 * 4).reshape((128, 4)).astype(np.int32)
expected = array_ops.gather_v2(params, indices, batch_dims=1, axis=1)

params = numpy_util.pack_numpy(
    params,
    layout=Layout([layout_lib.UNSHARDED, layout_lib.UNSHARDED, _MESH_DIM_X],
                  self.mesh))
indices = numpy_util.pack_numpy(
    indices, Layout([layout_lib.UNSHARDED, layout_lib.UNSHARDED],
                    self.mesh))

expected_layout = Layout(
    [layout_lib.UNSHARDED, layout_lib.UNSHARDED, _MESH_DIM_X], self.mesh)
with api.run_on(self.mesh):
    dtensor_result = array_ops.gather_v2(
        params, indices, batch_dims=1, axis=1)
    self.assertDTensorEqual(expected, expected_layout, dtensor_result)
