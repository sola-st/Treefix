# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
for adjoint_a in [True, False]:
    for adjoint_b in [True, False]:
        name = "sparse_tensor_dense_matmul_%s_%s_%s_%s" % (
            adjoint_a, adjoint_b, values_dtype.__name__, indices_dtype.__name__)
        self._testGradients(adjoint_a, adjoint_b, name, values_dtype,
                            indices_dtype)
