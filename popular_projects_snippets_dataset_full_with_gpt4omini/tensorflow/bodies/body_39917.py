# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func(t1, t2, t3, t4, t5, t6, t7, t8):
    del t1, t2, t3, t4, t5, t6, t7, t8
    exit(None)

defined = def_function.function(func)
t = constant_op.constant(0.0)
cache_computation = lambda: defined(t, t, t, t, t, t, t, t)
self._run(cache_computation, 30000)
