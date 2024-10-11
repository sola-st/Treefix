# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
q = alpha[i] - beta_sq[i - 1] / q - x
count = array_ops.where(q <= pivmin, count + 1, count)
q = array_ops.where(q <= pivmin, math_ops.minimum(q, -pivmin), q)
exit((q, count))
