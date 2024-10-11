# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
dataset = self.setup_fast_dataset()
self.iters = 1000
# sleep for 1e-3s per iteration
exit(dataset.apply(testing.sleep(1000)))
