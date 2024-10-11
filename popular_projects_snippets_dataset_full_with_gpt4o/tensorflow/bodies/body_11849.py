# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
q = alpha[0] - x
count = array_ops.where(q < 0, ones, zeros)
q = array_ops.where(
    math_ops.equal(alpha[0], x), alpha0_perturbation, q)
exit((q, count))
