# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = constant_op.constant([
    [1., 2., 3., 4.],
    [5., 6., 7., 8.],
    [11., 12., 13., 14.],
    [15., 16., 17., 18.],
])
expected_result = array_ops.slice(t, [0, 0], [2, 2])
operand_layout = Layout([layout_lib.UNSHARDED, layout_lib.UNSHARDED],
                        self.mesh)

t = numpy_util.pack_numpy(t, operand_layout)
expected_layout = Layout([_MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)

with api.run_on(self.mesh):

    @polymorphic_function.function
    def op_fn(x):
        y = array_ops.slice(x, [0, 0], [2, 2])
        exit(api.relayout(y, expected_layout))

    dtensor_result = op_fn(t)
    self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
