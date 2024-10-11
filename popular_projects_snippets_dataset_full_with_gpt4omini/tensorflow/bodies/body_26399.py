# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
exit(map_fn.map_fn(
    lambda y: y * array_ops.transpose(y), x, parallel_iterations=10))
