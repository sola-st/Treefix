# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
original_a = np.arange(5 * 4 * 6).reshape((5, 4, 6)).astype(np.float32)

original_layout = Layout([layout_lib.UNSHARDED, _MESH_DIM_Y, _MESH_DIM_X],
                         self.mesh)

# paris of (perm, expected_layout)
combinations = [
    ([2, 0, 1], [_MESH_DIM_X, layout_lib.UNSHARDED, _MESH_DIM_Y]),
    ([2, 1, 0], [_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED]),
    ([1, 2, 0], [_MESH_DIM_Y, _MESH_DIM_X, layout_lib.UNSHARDED]),
    ([1, 0, 2], [_MESH_DIM_Y, layout_lib.UNSHARDED, _MESH_DIM_X]),
    ([0, 1, 2], [layout_lib.UNSHARDED, _MESH_DIM_Y, _MESH_DIM_X]),
    ([0, 2, 1], [layout_lib.UNSHARDED, _MESH_DIM_X, _MESH_DIM_Y]),
]

for (perm, expected_spec) in combinations:
    a = original_a
    expected = array_ops.transpose_v2(a, perm)

    a = numpy_util.pack_numpy(a, original_layout)
    expected_layout = Layout(expected_spec, self.mesh)
    with api.run_on(self.mesh):
        dtensor_result = array_ops.transpose_v2(a, perm)
        self.assertDTensorEqual(expected, expected_layout, dtensor_result)
