# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/conjugate_gradient_test.py
np.random.seed(1)
a_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)
# Make a self-adjoint, positive definite.
a_np = np.dot(a_np.T, a_np)
# jacobi preconditioner
jacobi_np = np.zeros_like(a_np)
jacobi_np[range(a_np.shape[0]), range(a_np.shape[1])] = (
    1.0 / a_np.diagonal())
rhs_np = np.random.uniform(
    low=-1.0, high=1.0, size=shape_[0]).astype(dtype_)
x_np = np.zeros_like(rhs_np)
tol = 1e-6 if dtype_ == np.float64 else 1e-3
max_iter = 20
if use_static_shape_:
    a = constant_op.constant(a_np)
    rhs = constant_op.constant(rhs_np)
    x = constant_op.constant(x_np)
    jacobi = constant_op.constant(jacobi_np)
else:
    a = array_ops.placeholder_with_default(a_np, shape=None)
    rhs = array_ops.placeholder_with_default(rhs_np, shape=None)
    x = array_ops.placeholder_with_default(x_np, shape=None)
    jacobi = array_ops.placeholder_with_default(jacobi_np, shape=None)
operator = linalg.LinearOperatorFullMatrix(
    a, is_positive_definite=True, is_self_adjoint=True)
preconditioners = [
    None,
    # Preconditioner that does nothing beyond change shape.
    linalg.LinearOperatorIdentity(
        a_np.shape[-1],
        dtype=a_np.dtype,
        is_positive_definite=True,
        is_self_adjoint=True),
    # Jacobi preconditioner.
    linalg.LinearOperatorFullMatrix(
        jacobi,
        is_positive_definite=True,
        is_self_adjoint=True),
]
cg_results = []
for preconditioner in preconditioners:
    cg_graph = conjugate_gradient.conjugate_gradient(
        operator,
        rhs,
        preconditioner=preconditioner,
        x=x,
        tol=tol,
        max_iter=max_iter)
    cg_val = self.evaluate(cg_graph)
    norm_r0 = np.linalg.norm(rhs_np)
    norm_r = np.linalg.norm(cg_val.r)
    self.assertLessEqual(norm_r, tol * norm_r0)
    # Validate that we get an equally small residual norm with numpy
    # using the computed solution.
    r_np = rhs_np - np.dot(a_np, cg_val.x)
    norm_r_np = np.linalg.norm(r_np)
    self.assertLessEqual(norm_r_np, tol * norm_r0)
    cg_results.append(cg_val)
# Validate that we get same results using identity_preconditioner
# and None
self.assertEqual(cg_results[0].i, cg_results[1].i)
self.assertAlmostEqual(cg_results[0].gamma, cg_results[1].gamma)
self.assertAllClose(cg_results[0].r, cg_results[1].r, rtol=tol)
self.assertAllClose(cg_results[0].x, cg_results[1].x, rtol=tol)
self.assertAllClose(cg_results[0].p, cg_results[1].p, rtol=tol)
