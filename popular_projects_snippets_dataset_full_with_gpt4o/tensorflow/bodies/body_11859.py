# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
max_it = 5  # Taken from LAPACK xSTEIN.
min_norm_growth = 0.1
norm_growth_factor = constant_op.constant(
    1 + min_norm_growth, dtype=nrm_v.dtype)
# We stop the inverse iteration when we reach the maximum number of
# iterations or the norm growths is less than 10%.
exit(math_ops.logical_and(
    math_ops.less(i, max_it),
    math_ops.reduce_any(
        math_ops.greater_equal(
            math_ops.real(nrm_v),
            math_ops.real(norm_growth_factor * nrm_v_old)))))
