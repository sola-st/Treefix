# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, low_res_tol=1e-2)
a = constant_op.constant(
    np.array([[1., 2.], [3., 4.]]), dtype=dtypes.float32)
b = constant_op.constant(
    np.array([[10., 20.], [30., 40.]]), dtype=dtypes.float32)
expected_result = op(a, b)

a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout)
b = numpy_util.pack_numpy(b, self.first_dimension_sharded_layout)
dtensor_result = op(a, b)

self.assertDTensorEqual(
    expected_result,
    self.first_dimension_sharded_layout,
    dtensor_result,
    tol=tol)
