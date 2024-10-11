# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
for i, version in enumerate(
    [NON_PARALLEL, EXPERIMENTAL_PARALLEL, CORE_PARALLEL]):
    self._benchmark(
        interleave_version=version,
        cycle_length=1,
        num_elements=200000,
        name="single_cycle_" + version,
        benchmark_id=i,
        benchmark_label="single_cycle")
