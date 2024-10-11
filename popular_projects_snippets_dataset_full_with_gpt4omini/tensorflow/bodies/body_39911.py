# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda: array_ops.transpose(m, perm, conjugate)
self._run(func, num_iters, execution_mode=execution_mode)
