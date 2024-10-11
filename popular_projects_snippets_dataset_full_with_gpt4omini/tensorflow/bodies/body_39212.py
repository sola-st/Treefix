# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
print("DenseDense MatMul (w/ Sparse Flag) vs. SparseTensorDense MatMul")
print("Matrix sizes:")
print("  A sparse [m, k] with % nonzero values between 1% and 80%")
print("  B dense [k, n]")
print("")
print("% nnz \t n \t gpu \t m \t k \t dt(dense) \t dt(sparse) "
      "\t dt(sparse)/dt(dense)")

for thresh in (0.99, 0.8, 0.5, 0.2):
    for n in (50, 100):
        for use_gpu in (True, False):
            for m in (100, 1000):
                for k in (100, 1000):
                    sparse_tensor_dense_vs_dense_matmul_benchmark(
                        thresh, m, k, n, False, False, use_gpu=use_gpu)
