# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py

def CompareNonEmpty(self, a_shape, b_shape):
    self._compare(
        GetRandomNormalInput(a_shape, dtype),
        GetRandomNormalInput(b_shape, dtype),
        adjoint_a,
        adjoint_b,
        static_shape=use_static_shape)

CompareNonEmpty(self, [1, 2, 3], [1, 3, 5])
CompareNonEmpty(self, [1, 2, 3], [1, 3, 1])
CompareNonEmpty(self, [1, 1, 3], [1, 3, 5])
CompareNonEmpty(self, [1, 2, 3], [1, 3, 5])
CompareNonEmpty(self, [7, 1, 3], [7, 3, 5])
CompareNonEmpty(self, [7, 2, 3], [7, 3, 1])
CompareNonEmpty(self, [7, 2, 3], [7, 3, 5])
CompareNonEmpty(self, [10, 64, 75], [10, 75, 30])
CompareNonEmpty(self, [5, 7, 2, 3], [5, 7, 3, 5])
