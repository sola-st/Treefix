# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/optimize_benchmark.py
chain_lengths = [0, 1, 2, 5, 10, 20, 50]
for chain_length in chain_lengths:
    self._benchmark_filter_parallelization(
        chain_length=chain_length, optimize_dataset=False)
    self._benchmark_filter_parallelization(
        chain_length=chain_length, optimize_dataset=True)
