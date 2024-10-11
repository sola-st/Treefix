# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
for i, version in enumerate([EXPERIMENTAL_PARALLEL, CORE_PARALLEL]):
    self._benchmark(
        interleave_version=version,
        num_elements=200000,
        name="fast_input_" + version,
        benchmark_id=i,
        benchmark_label="fast_input")
