# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
self._compare(
    GetRandomNormalInput(a_shape, dtype),
    GetRandomNormalInput(b_shape, dtype),
    adjoint_a,
    adjoint_b,
    static_shape=use_static_shape)
