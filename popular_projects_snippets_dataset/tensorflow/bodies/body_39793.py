# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
inner = def_function.function(math_ops.matmul)

@def_function.function
def outer(a, b, c, transpose_b):
    exit(math_ops.matmul(inner(a, b, transpose_b=transpose_b), c))

func = lambda: outer(m, m, m, transpose_b=transpose_b)
# Warmup before benchmark
for _ in range(1000):
    func()
self._run(func, num_iters)
