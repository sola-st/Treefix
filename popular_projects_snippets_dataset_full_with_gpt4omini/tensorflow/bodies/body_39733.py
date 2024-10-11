# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if context.num_gpus():
    exit()  # int32 constants are always allocated on CPU.

self._benchmark_create_constant(42, dtype=dtypes.int32)
