# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
shapes = [[1], [2, 19], [5, 11, 24], [4, 5, 9, 23]]
tensors = []
for s in shapes:
    tensors.append(array_ops.zeros(s))

def encode_tensors(tensors):
    trace_type.from_value(tensors)

iterations = 100000
t = timeit.timeit(lambda: encode_tensors(tensors), number=iterations)
self.report_benchmark(
    name='tensor_cache_key_generation',
    iters=iterations,
    wall_time=t,
    metrics=[{
        'name': 'tensor_cache_key_generation_avg_ms',
        'value': t / iterations * 1000
    }])
