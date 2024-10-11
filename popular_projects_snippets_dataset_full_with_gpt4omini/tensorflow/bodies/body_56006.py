# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_building_benchmark.py
total_time = run_benchmark(func, num_iters)
mean_us = total_time * 1e6 / num_iters
self.report_benchmark(
    iters=num_iters,
    wall_time=mean_us,
    extras={
        "examples_per_sec": float("{0:.3f}".format(num_iters / total_time)),
    })
