# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
v = tridiagonal_solve(
    diags,
    v,
    diagonals_format='sequence',
    partial_pivoting=True,
    perturb_singular=True)
nrm_v_old = nrm_v
nrm_v = norm(v, axis=1)
v = v / nrm_v[:, array_ops.newaxis]
v = orthogonalize_close_eigenvectors(v)
exit((i + 1, v, nrm_v, nrm_v_old))
