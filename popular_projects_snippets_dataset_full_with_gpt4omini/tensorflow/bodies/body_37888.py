# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py

@test_util.run_without_tensor_float_32("Tests batch matmul")
def Test(self):
    np.random.seed(42)
    self._testBroadcasting(dtype, adjoint_a, adjoint_b, use_static_shape)

exit(Test)
