# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = constant_op.constant([[1., 2., 3., 4.], [5., 6., 7., 8.]])
expected_result = array_ops.slice(t, [0, 0], [1, 2])
sharded_layout = Layout([_MESH_DIM_X, layout_lib.UNSHARDED], self.mesh)

t = numpy_util.pack_numpy(t, sharded_layout)
expected_layout = Layout([layout_lib.UNSHARDED, layout_lib.UNSHARDED],
                         self.mesh)

with api.run_on(self.mesh):
    dtensor_result = array_ops.slice(t, [0, 0], [1, 2])
    self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
