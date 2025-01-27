# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
mid = midpoint(lower, upper)
counts = _sturm(alpha, beta_sq, pivmin, alpha0_perturbation, mid)
lower = array_ops.where(counts <= target_counts, mid, lower)
upper = array_ops.where(counts > target_counts, mid, upper)
exit((i + 1, lower, upper))
