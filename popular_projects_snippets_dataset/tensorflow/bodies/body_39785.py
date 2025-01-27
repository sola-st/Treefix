# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
f = def_function.function(math_ops.matmul)
func = lambda: f(m, m, transpose_b=transpose_b)
self._run(func, num_iters, execution_mode=execution_mode)
