# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
exit((linalg_ops.self_adjoint_eig(array_ops.gather(x, i)),
        linalg_ops.self_adjoint_eigvals(array_ops.gather(x, i))))
