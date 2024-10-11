# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
self._compare(
    np.zeros(a_shape).astype(dtype),
    np.zeros(b_shape).astype(dtype),
    adjoint_a,
    adjoint_b,
    static_shape=use_static_shape)
