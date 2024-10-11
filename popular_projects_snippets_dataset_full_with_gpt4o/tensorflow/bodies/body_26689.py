# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/autotune_benchmark.py
a = self._benchmark_interleave(autotune=False, benchmark_id=1)
b = self._benchmark_interleave(autotune=True, benchmark_id=2)
print("autotune parallelism vs no autotuning speedup: {}".format(a / b))
