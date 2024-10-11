# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, 1e-3)
a = constant_op.constant(np.arange(6).reshape((2, 3)), dtype=dtypes.float32)
expected_result = op(a)

a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout)
dtensor_result = op(a)

self.assertDTensorEqual(
    expected_result,
    self.first_dimension_sharded_layout,
    dtensor_result,
    tol=tol)
