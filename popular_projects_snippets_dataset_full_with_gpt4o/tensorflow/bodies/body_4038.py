# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, low_res_tol=1e-2)
# Currently we only support scalar.
a = constant_op.constant(23.4)
b = constant_op.constant(
    10.0 * np.arange(8).reshape((2, 4)), dtype=dtypes.float32)
expected_result = op(a, b)

a = api.copy_to_mesh(a, self.scalar_replicated_layout)
sharded_layout_2d = Layout([_MESH_DIM_X, _MESH_DIM_Y], self.mesh)
b = numpy_util.pack_numpy(b, sharded_layout_2d)

dtensor_result = op(a, b)

self.assertDTensorEqual(
    expected_result, sharded_layout_2d, dtensor_result, tol=tol)
