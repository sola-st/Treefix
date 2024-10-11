# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test.py
print("Sparse Xent vs. SparseToDense + Xent")
print("batch \t depth \t gpu \t dt(dense) \t dt(sparse) "
      "\t dt(sparse)/dt(dense)")
for use_gpu in (False, True):
    for batch_size in (32, 64, 128):
        for num_entries in (100, 1000, 10000):
            sparse_vs_dense_xent_benchmark(batch_size, num_entries, use_gpu)
    sparse_vs_dense_xent_benchmark(32, 100000, use_gpu)
    sparse_vs_dense_xent_benchmark(8, 1000000, use_gpu)
