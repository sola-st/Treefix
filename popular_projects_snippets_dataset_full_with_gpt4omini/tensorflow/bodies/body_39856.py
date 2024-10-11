# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
with context.device(device):
    x = constant_op.constant([[1, 0.], [0., 0.]])
    if defunc:
        reduce_func = def_function.function(
            math_ops.reduce_logsumexp, jit_compile=xla_compile)
        func = lambda: reduce_func(x)
    else:
        func = lambda: math_ops.reduce_logsumexp(x)
    self._run(func, 3000, execution_mode=execution_mode)
