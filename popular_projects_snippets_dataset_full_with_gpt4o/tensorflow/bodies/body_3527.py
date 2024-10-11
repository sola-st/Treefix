# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
# If there are 50 keys and we get a new key that is equal to a key that is
# in the cache.

cache = function_cache.FunctionCache()
args_per_call = 5
num_total_checks = 50

keys = []
for i in range(num_total_checks):
    args = []
    for j in range(args_per_call):
        args.append(array_ops.zeros([i, j]))
    keys.append(make_type_and_deleter(args))

for key in keys:
    cache.add(make_none_context(), *key, "testing")

iterations = 10000
subtyping_time = timeit.timeit(
    lambda: cache.lookup(make_none_context(), keys[-1][0]),
    number=iterations)
equality_time = timeit.timeit(
    lambda: cache.lookup(make_none_context(), keys[-1][0]),
    number=iterations)

self.report_benchmark(
    name="cache_hit_50th_f_type_equal",
    iters=iterations,
    wall_time=subtyping_time + equality_time,
    metrics=[{
        "name": "cache_hit_50th_f_type_equal_subtype_avg_ms",
        "value": subtyping_time / iterations * 1000
    }, {
        "name": "cache_hit_50th_f_type_equal_equality_avg_ms",
        "value": equality_time / iterations * 1000
    }, {
        "name": "cache_hit_50th_f_type_subtype_over_equality_ratio",
        "value": subtyping_time / equality_time
    }])
