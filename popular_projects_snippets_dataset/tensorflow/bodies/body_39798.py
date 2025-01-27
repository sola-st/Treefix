# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with backprop.GradientTape() as tape:
    tape.watch(m)
    self._benchmark_gen_math_ops_matmul(
        m, transpose_b=False, num_iters=num_iters)
