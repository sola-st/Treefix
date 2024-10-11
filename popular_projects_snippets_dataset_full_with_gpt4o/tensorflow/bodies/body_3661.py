# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
var_list = [
    variables.Variable(1.0),
    variables.Variable(1),
    variables.Variable([1])
]

def encode_variables(var_list):
    trace_type.from_value(var_list)

iterations = 10000
t = timeit.timeit(lambda: encode_variables(var_list), number=iterations)
self.report_benchmark(
    name='variable_cache_key_generation',
    iters=iterations,
    wall_time=t,
    metrics=[{
        'name': 'variable_cache_key_generation_avg_ms',
        'value': t / iterations * 1000
    }])
