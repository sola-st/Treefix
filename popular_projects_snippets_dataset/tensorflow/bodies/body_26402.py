# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
exit(dataset_ops.Dataset.range(num_map_elements).map(
    g, num_parallel_calls=num_parallel_calls))
