# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py

print("SparseAddDense: add with sparse_to_dense vs. sparse_add")
print("%nnz \t n \t m \t millis(s2d) \t millis(sparse_add) \t speedup")

for sparsity in [0.99, 0.5, 0.01]:
    for n in [1, 256, 50000]:
        for m in [100, 1000]:
            s2d_dt, sa_dt = _s2d_add_vs_sparse_add(sparsity, n, m)
            print("%.2f \t %d \t %d \t %.4f \t %.4f \t %.2f" % (sparsity, n, m,
                                                                s2d_dt, sa_dt,
                                                                s2d_dt / sa_dt))
