# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
for i, version in enumerate([EXPERIMENTAL_PARALLEL, CORE_PARALLEL]):
    self._benchmark(
        interleave_version=version,
        cycle_length=1000,
        num_elements=100000,
        name="long_cycle_" + version,
        benchmark_id=i,
        benchmark_label="long_cycle")
