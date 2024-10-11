# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
cycle_lengths = [None, 100]
nums_parallel_calls = [None, 1, 10, 100, dataset_ops.AUTOTUNE]
for cycle_length in cycle_lengths:
    for num_parallel_calls in nums_parallel_calls:
        self._benchmark_nested_parallel_map(cycle_length, num_parallel_calls)
