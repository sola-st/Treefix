# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant([[1., 2.], [3., 4.]])
assert a.shape == [2, 2]
expected_result = op(a)

a = api.copy_to_mesh(a, self.replicated_layout_2d)
dtensor_result = op(a)

tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, 1e-4)
self.assertDTensorEqual(
    expected_result, self.replicated_layout_2d, dtensor_result, tol=tol)
