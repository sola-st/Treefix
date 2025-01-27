# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
e, v = linalg_ops.self_adjoint_eig(x)
# (complex) Eigenvectors are only unique up to an arbitrary phase
# We normalize the vectors such that the first component has phase 0.
top_rows = v[..., 0:1, :]
if dtype_.is_complex:
    angle = -math_ops.angle(top_rows)
    phase = math_ops.complex(math_ops.cos(angle), math_ops.sin(angle))
else:
    phase = math_ops.sign(top_rows)
v *= phase
exit((e, v))
