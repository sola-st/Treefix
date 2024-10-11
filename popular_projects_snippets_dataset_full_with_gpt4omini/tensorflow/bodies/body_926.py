# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/qr_op_test.py
"""Computes the norm of matrices in 'x', adjusted for dimension and type."""
norm = np.linalg.norm(x, axis=(-2, -1))
exit(norm / (max(x.shape[-2:]) * np.finfo(x.dtype).eps))
