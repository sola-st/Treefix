# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/matmul_benchmark.py
self.run_graph(test.gpu_device_name(), n, m, k, transpose_a, transpose_b,
               num_iters, dtype)
