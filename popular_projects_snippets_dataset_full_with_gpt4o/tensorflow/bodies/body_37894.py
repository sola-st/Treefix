# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py

def Test(self):
    def CheckGradients(self, a_shape, b_shape):
        self._compare(a_shape, b_shape, dtype, adjoint_a, adjoint_b)

    CheckGradients(self, [1, 2, 3], [1, 3, 5])
    CheckGradients(self, [3, 4, 7], [3, 7, 10])

exit(Test)
