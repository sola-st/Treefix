# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/conjugate_gradient.py
exit(array_ops.squeeze(
    math_ops.matvec(
        x[..., array_ops.newaxis],
        y, adjoint_a=True), axis=-1))
