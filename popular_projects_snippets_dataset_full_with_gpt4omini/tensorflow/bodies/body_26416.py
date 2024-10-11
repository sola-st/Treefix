# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/interleave_benchmark.py
for i, version in enumerate([EXPERIMENTAL_PARALLEL, CORE_PARALLEL]):
    self._benchmark(
        interleave_version=version,
        initial_delay_us=100 * 1000,
        remainder_delay_us=1000,
        num_elements=5000,
        name="remote_file_simulation_" + version,
        benchmark_id=i,
        benchmark_label="remote_file")
