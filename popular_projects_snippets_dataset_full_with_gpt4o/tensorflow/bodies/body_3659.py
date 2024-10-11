# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
shapes = [[1], [2, 19], [5, 11, 24], [4, 5, 9, 23]]
tensor_specs = []
for s in shapes:
    tensor_specs.append(tensor_spec.TensorSpec(s, dtypes.int32))

def encode_tensor_specs(tensor_specs):
    trace_type.from_value(tensor_specs)

iterations = 100000
t = timeit.timeit(
    lambda: encode_tensor_specs(tensor_specs), number=iterations)
self.report_benchmark(
    name='tensor_spec_cache_key_generation',
    iters=iterations,
    wall_time=t,
    metrics=[{
        'name': 'tensor_spec_cache_key_generation_avg_ms',
        'value': t / iterations * 1000
    }])
