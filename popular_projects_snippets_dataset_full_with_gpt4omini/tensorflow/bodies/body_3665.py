# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
struct = {(1, 2, 3): {(1, 2): {12: 2}}, (3, 2, 3): (2, {2: 3})}

def encode_struct(struct):
    trace_type.from_value(struct)

iterations = 100000
t = timeit.timeit(lambda: encode_struct(struct), number=iterations)
self.report_benchmark(
    name='nested_struct_cache_key_generation',
    iters=iterations,
    wall_time=t,
    metrics=[{
        'name': 'nested_struct_cache_key_generation_avg_ms',
        'value': t / iterations * 1000
    }])
