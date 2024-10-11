# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_sparse_mat_mul_grad_test.py
super(CSRSparseMatrixGradTest, cls).setUpClass()
cls._gpu_available = test_util.is_gpu_available()
