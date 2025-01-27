# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
gc.disable()
gc.collect()
self.run_report(_run_benchmark, func, num_iters)
gc.enable()
