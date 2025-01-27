# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda: math_ops.matmul(m, m, transpose_b=transpose_b)
self._run(func, num_iters, execution_mode=execution_mode)
