# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py

def Test(self):
    def CheckGradients(self, a_shape, b_shape):
        self._compare(a_shape, b_shape, dtype, adjoint_a, adjoint_b)

    CheckGradients(self, [1, 5, 2, 3], [7, 1, 3, 2])
    CheckGradients(self, [2, 3], [1, 3, 5])
    CheckGradients(self, [2, 3], [5, 3, 5])
    CheckGradients(self, [5, 2, 5], [5, 3])
    CheckGradients(self, [5, 2, 2, 3], [3, 5])
    CheckGradients(self, [4, 5, 1, 2, 3], [1, 1, 3, 5])
    CheckGradients(self, [1, 2, 1, 4, 2, 1, 3, 4], [3, 2, 1, 1, 1, 2, 4, 2])

exit(Test)
