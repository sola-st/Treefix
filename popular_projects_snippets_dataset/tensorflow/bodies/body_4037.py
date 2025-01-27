# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
tol = select_tol(op, self.mesh, test_util.DEFAULT_TOL, low_res_tol=1e-2)
# Currently we only support scalar.
a = constant_op.constant(3)
b = constant_op.constant([[0, 1], [2, 3]])
a, b = order_broadcastable_operands(op, a, b)
expected_result = op(a, b)

a = api.copy_to_mesh(a, self.scalar_replicated_layout)
b = api.copy_to_mesh(b, self.replicated_layout_2d)
dtensor_result = op(a, b)

self.assertDTensorEqual(
    expected_result, self.replicated_layout_2d, dtensor_result, tol=tol)
