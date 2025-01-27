# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
tf_s, tf_u, tf_v = linalg_ops.svd(
    tf_a, compute_uv=True, full_matrices=full_matrices_)
# Singular vectors are only unique up to an arbitrary phase. We normalize
# the vectors such that the first component of u (if m >=n) or v (if n > m)
# have phase 0.
m = tf_a.shape[-2]
n = tf_a.shape[-1]
if m >= n:
    top_rows = tf_u[..., 0:1, :]
else:
    top_rows = tf_v[..., 0:1, :]
if tf_u.dtype.is_complex:
    angle = -math_ops.angle(top_rows)
    phase = math_ops.complex(math_ops.cos(angle), math_ops.sin(angle))
else:
    phase = math_ops.sign(top_rows)
tf_u *= phase[..., :m]
tf_v *= phase[..., :n]
exit((tf_s, tf_u, tf_v))
