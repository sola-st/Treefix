# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
with context.eager_mode():
    dataset = self.setup_fast_dataset()
    self.run_benchmark_in_eager(dataset)
