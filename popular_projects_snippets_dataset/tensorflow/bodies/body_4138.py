# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
params = np.arange(128 * 1000 * 32).reshape(
    (128, 1000, 32)).astype(np.float32)
indices = np.random.randint(
    0, 32, size=128 * 4 * 4).reshape((128, 4, 4)).astype(np.int32)
expected = array_ops.gather_v2(params, indices, batch_dims=1, axis=2)

params = numpy_util.pack_numpy(
    params,
    layout=Layout([_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED],
                  self.mesh))
indices = numpy_util.pack_numpy(
    indices,
    Layout(
        [layout_lib.UNSHARDED, layout_lib.UNSHARDED, layout_lib.UNSHARDED],
        self.mesh))

expected_layout = Layout(
    [_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED, layout_lib.UNSHARDED],
    self.mesh)
with api.run_on(self.mesh):
    dtensor_result = array_ops.gather_v2(
        params, indices, batch_dims=1, axis=2)
    self.assertDTensorEqual(expected, expected_layout, dtensor_result)
