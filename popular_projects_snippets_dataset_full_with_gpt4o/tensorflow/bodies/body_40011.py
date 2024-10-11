# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func(lim):
    exit(math_ops.range(lim, dtype=dtype))

compiled_func = def_function.function(func)

with context.device(device):
    limit_t = constant_op.constant(limit, dtype=dtype)
    compiled_func(limit_t)
    self._run(lambda: compiled_func(limit_t), num_iters=num_iters)
