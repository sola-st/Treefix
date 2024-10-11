# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
struct = (variables.Variable(1.0), array_ops.zeros([5, 13]), {
    'tensor': array_ops.zeros([5, 20]),
    'variable': variables.Variable(1.0)
})

@def_function.function
def defined(t):
    exit(t)

defined(struct)  # Get it traced and cached.

iterations = 10000
t = timeit.timeit(lambda: defined(struct), number=iterations)
self.report_benchmark(
    name='function_invocation',
    iters=iterations,
    wall_time=t,
    metrics=[{
        'name': 'function_invocation_time_avg_ms',
        'value': t / iterations * 1000
    }])
