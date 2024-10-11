# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant([[[1.], [2.], [3.], [4.]], [[5.], [6.], [7.],
                                                     [8.]]])
assert a.shape == [2, 4, 1]
expected_result = op(a)

layout = Layout([_MESH_DIM_X, _MESH_DIM_Y, layout_lib.UNSHARDED], self.mesh)
a = numpy_util.pack_numpy(a, layout)
dtensor_result = op(a)

tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, 1e-4)
self.assertDTensorEqual(expected_result, layout, dtensor_result, tol=tol)
