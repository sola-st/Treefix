# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, low_res_tol=1e-2)
a = constant_op.constant(np.arange(8).reshape((2, 4)), dtype=dtypes.float32)
b = constant_op.constant(
    np.arange(8).reshape((2, 4)) + 10.0, dtype=dtypes.float32)
expected_result = op(a, b)

sharded_layout_2d = Layout([_MESH_DIM_X, _MESH_DIM_Y], self.mesh)
a = numpy_util.pack_numpy(a, sharded_layout_2d)
b = numpy_util.pack_numpy(b, sharded_layout_2d)
dtensor_result = op(a, b)

self.assertDTensorEqual(
    expected_result, sharded_layout_2d, dtensor_result, tol=tol)
