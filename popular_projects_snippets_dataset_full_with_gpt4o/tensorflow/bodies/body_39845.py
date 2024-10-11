# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with ops.device(CPU):
    matmul = def_function.function(math_ops.matmul)

    @def_function.function()
    def compiled_function(x, tangent):
        with forwardprop.ForwardAccumulator(x, tangent) as acc:
            result = matmul(x, x, transpose_b=True)
        exit((result, acc.jvp(result)))

    m = random_ops.random_uniform(shape).cpu()
    tangent = random_ops.random_uniform(shape).cpu()
    func = lambda: compiled_function(m, tangent)

    # Warmup before benchmark
    for _ in range(100):
        func()
    self._run(func, 3000)
