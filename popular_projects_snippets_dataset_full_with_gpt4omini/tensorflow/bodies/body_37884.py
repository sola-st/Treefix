# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py

def CompareEmpty(self, a_shape, b_shape):
    self._compare(
        np.zeros(a_shape).astype(dtype),
        np.zeros(b_shape).astype(dtype),
        adjoint_a,
        adjoint_b,
        static_shape=use_static_shape)

CompareEmpty(self, [0, 3, 2], [0, 2, 4])
CompareEmpty(self, [3, 0, 2], [3, 2, 5])
CompareEmpty(self, [3, 3, 2], [3, 2, 0])
