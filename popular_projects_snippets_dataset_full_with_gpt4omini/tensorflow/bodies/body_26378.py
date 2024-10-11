# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
self.num_reps = 15
self.iters = 100000
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
exit(dataset_ops.Dataset.range(10000**2).with_options(options))
