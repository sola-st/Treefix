# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
op = gen_nn_ops.relu

a = constant_op.constant([[[1.], [-2.], [3.], [-4.]],
                          [[5.], [-6.], [-7.], [8.]]])
assert a.shape == [2, 4, 1]
expected_result = op(a)

init_layout = Layout([_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED],
                     self.mesh)
a = numpy_util.pack_numpy(a, init_layout)
dtensor_output = op(a)

final_layout = Layout(
    [_MESH_DIM_X, layout_lib.UNSHARDED, layout_lib.UNSHARDED], self.mesh)
# eager relayout
dtensor_result = api.relayout(dtensor_output, final_layout)
self.assertDTensorEqual(expected_result, final_layout, dtensor_result)
