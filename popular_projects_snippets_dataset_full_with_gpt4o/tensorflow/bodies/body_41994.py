# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
total_time = run_benchmark(func, num_iters, execution_mode)
mean_us = total_time * 1e6 / num_iters
self.report_benchmark(
    iters=num_iters,
    wall_time=mean_us,
    extras={"examples_per_sec": num_iters / total_time})
