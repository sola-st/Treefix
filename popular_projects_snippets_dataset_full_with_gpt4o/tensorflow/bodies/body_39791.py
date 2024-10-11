# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

@def_function.function
def defun_matmul(m):
    exit(math_ops.matmul(m, m))

func = lambda: defun_matmul(m)
self._run(func, num_iters, execution_mode=execution_mode)
