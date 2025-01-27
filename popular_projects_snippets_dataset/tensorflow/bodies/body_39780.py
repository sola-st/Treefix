# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func():
    gen_math_ops.mat_mul(m, m, transpose_b=transpose_b)

self._run(func, num_iters)
