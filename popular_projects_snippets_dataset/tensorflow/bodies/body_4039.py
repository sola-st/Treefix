# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, low_res_tol=1e-2)
# Currently we only support scalar.
a = constant_op.constant(23.4)
b = constant_op.constant(
    np.array([[10., 20.], [30., 40.]]), dtype=dtypes.float32)
expected_result = op(a, b)

a = api.copy_to_mesh(a, self.scalar_replicated_layout)
b = numpy_util.pack_numpy(b, self.first_dimension_sharded_layout)

dtensor_result = op(a, b)

self.assertDTensorEqual(
    expected_result,
    self.first_dimension_sharded_layout,
    dtensor_result,
    tol=tol)
