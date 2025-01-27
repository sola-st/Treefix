# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
f = def_function.function(math_ops.matmul)

def func():
    with backprop.GradientTape() as gt:
        gt.watch(m)
        y = f(m, m, transpose_b=transpose_b)
    _ = gt.gradient(y, m)

self._run(func, num_iters, execution_mode=execution_mode)
