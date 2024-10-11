# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with ops.device(CPU):
    m = random_ops.random_uniform(shape).cpu()
    tangent = random_ops.random_uniform(shape).cpu()
    matmul = def_function.function(math_ops.matmul)

    def func():
        with forwardprop.ForwardAccumulator(m, tangent) as acc:
            result = matmul(m, m, transpose_b=True)
        exit((result, acc.jvp(result)))

    # Warmup before benchmark
    for _ in range(100):
        func()
    self._run(func, 3000)
