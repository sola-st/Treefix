# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func(v, lim):
    for _ in math_ops.range(lim, dtype=range_dtype):
        v.assign_add(constant_op.constant(1, dtype=dtype))
    exit(v)

compiled_func = def_function.function(func)

with context.device(CPU):
    m = resource_variable_ops.ResourceVariable(
        constant_op.constant(1, dtype=dtype), dtype=dtype)
    limit_t = constant_op.constant(limit, dtype=dtype)

with context.device(device):
    compiled_func(m, limit_t)
    self._run(lambda: compiled_func(m, limit_t), num_iters=num_iters)
