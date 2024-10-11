# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
# If there are 50 keys and we get a key that has a subtype in cache and
# the cache has observed the key before (to memorize the subtype).

cache = function_cache.FunctionCache()
args_per_call = 5
num_total_checks = 50

keys = []
for i in range(num_total_checks - 1):
    args = []
    for j in range(args_per_call):
        args.append(array_ops.zeros([i, j]))
    keys.append(make_type_and_deleter(args))

for key in keys:
    cache.add(make_none_context(), *key, "testing")
cache.add(make_none_context(),
          make_single_param_type(MockSubtypeOf2(2)),
          trace_type.WeakrefDeletionObserver(), "testing")
cache.lookup(make_none_context(),
             make_single_param_type(MockSubtypeOf2(3)))

iterations = 10000
lookup_key = make_single_param_type(MockSubtypeOf2(2))
subtyping_time = timeit.timeit(
    lambda: cache.lookup(make_none_context(), lookup_key),
    number=iterations)

self.report_benchmark(
    name="cache_hit_50th_f_type_known_subtype",
    iters=iterations,
    wall_time=subtyping_time,
    metrics=[{
        "name": "cache_hit_50th_f_type_known_subtype_avg_ms",
        "value": subtyping_time / iterations * 1000
    }])
