# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
e, v = linalg_ops.eig(x)

# We sort eigenvalues by e.real+e.imag to have consistent
# order between runs
b_dims = len(e.shape) - 1
idx = sort_ops.argsort(math_ops.real(e) + math_ops.imag(e), axis=-1)
e = array_ops.gather(e, idx, batch_dims=b_dims)
v = array_ops.gather(v, idx, batch_dims=b_dims)

# (complex) Eigenvectors are only unique up to an arbitrary phase
# We normalize the vectors such that the first component has phase 0.
top_rows = v[..., 0:1, :]
angle = -math_ops.angle(top_rows)
phase = math_ops.complex(math_ops.cos(angle), math_ops.sin(angle))
v *= phase
exit((e, v))
