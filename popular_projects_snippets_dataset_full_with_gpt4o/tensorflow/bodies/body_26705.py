# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_defun_benchmark.py

wall_time = self.run_op_benchmark(op=op, iters=num_iters, warmup=True)
zero_division_delta = 1e-100
wall_time = wall_time + zero_division_delta
self.report_benchmark(
    name=name,
    iters=num_iters,
    wall_time=wall_time,
    extras={
        "examples_per_sec": 1 / float(wall_time),
        "model_name": "map_defun.benchmark.%d" % benchmark_id,
        "parameters": "%d" % num_iters,
    })
