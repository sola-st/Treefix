# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py

def CompareNonEmpty(self, a_shape, b_shape):
    self._compare(
        GetRandomNormalInput(a_shape, dtype),
        GetRandomNormalInput(b_shape, dtype),
        adjoint_a,
        adjoint_b,
        static_shape=use_static_shape)

CompareNonEmpty(self, [2, 3], [1, 3, 5])
CompareNonEmpty(self, [1, 2, 3], [3, 5])
CompareNonEmpty(self, [5, 1, 2, 3], [1, 7, 3, 5])
CompareNonEmpty(self, [5, 2, 2, 3], [3, 5])
CompareNonEmpty(self, [2, 3], [5, 2, 3, 5])
CompareNonEmpty(self, [4, 5, 1, 2, 3], [1, 1, 3, 5])
CompareNonEmpty(self, [1, 2, 1, 4, 2, 1, 3, 4], [3, 2, 1, 1, 1, 2, 4, 2])
