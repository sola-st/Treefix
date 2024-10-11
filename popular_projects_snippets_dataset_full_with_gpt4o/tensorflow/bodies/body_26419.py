# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
self._benchmark(
    interleave_version=CORE_PARALLEL,
    num_elements=200000,
    num_parallel_calls=1,
    name="single_parallel_call_" + CORE_PARALLEL,
    benchmark_id=1,
    benchmark_label="single_parallel_call")
