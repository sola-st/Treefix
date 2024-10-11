# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/conjugate_gradient.py
exit(math_ops.logical_and(
    i < max_iter,
    math_ops.reduce_any(linalg.norm(state.r, axis=-1) > tol)))
