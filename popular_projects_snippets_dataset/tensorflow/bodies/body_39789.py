# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

@def_function.function(reduce_retracing=True)
def defun_matmul(m):
    exit(math_ops.matmul(m, m))

m_3_by_3 = random_ops.random_uniform((3, 3))
defun_matmul(m_3_by_3)
func = lambda: defun_matmul(m)
self._run(func, num_iters, execution_mode=execution_mode)
