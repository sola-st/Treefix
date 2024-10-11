# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py

@def_function.function
def defined(t):
    exit(t)

call_arg_list = [
    1,
    array_ops.zeros([5, 13]),
    array_ops.zeros([9, 22, 24]),
    array_ops.zeros([5, 13, 2])
]

for c in call_arg_list:
    defined(c)

lookup_call_arg = array_ops.zeros([5, 13])

iterations = 10000
t = timeit.timeit(stmt=lambda: defined(lookup_call_arg), number=iterations)

self.report_benchmark(
    name='cache_key_lookup',
    iters=iterations,
    wall_time=t,
    metrics=[{
        'name': 'cache_key_lookup_avg_ms',
        'value': t / iterations * 1000
    }])
