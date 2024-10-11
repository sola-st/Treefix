# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func(c, lim):
    for _ in math_ops.range(lim, dtype=range_dtype):
        c += 1
    exit(c)

compiled_func = def_function.function(func)

with context.device(CPU):
    input_c = constant_op.constant(1, dtype=dtype)
    limit_t = constant_op.constant(limit, dtype=dtype)

with context.device(device):
    compiled_func(input_c, limit_t)
    self._run(lambda: compiled_func(input_c, limit_t), num_iters=num_iters)
